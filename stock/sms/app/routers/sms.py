from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
from typing import List
from ..models import SMSMessage, PhoneNumber, Merchant, User
from ..services import SMSService
from ..database import get_db_connection, release_db_connection
from ..auth import get_current_user
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/sms",
    tags=["SMS"]
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def sms_dashboard(request: Request, current_user: User = Depends(get_current_user)):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        
        if current_user.role == "Admin":
            query = sql.SQL("""
                SELECT pn.id, pn.number, c.name
                FROM phone_numbers pn
                LEFT JOIN customers c ON pn.customer_id = c.id
                WHERE pn.merchant_id = %s
                ORDER BY pn.number
            """)
            cursor.execute(query, (current_user.merchant_id,))
        
        elif current_user.role == "Operator":
            query = sql.SQL("""
                SELECT pn.id, pn.number, c.name
                FROM phone_numbers pn
                JOIN project_phone_numbers ppn ON pn.id = ppn.phone_number_id
                JOIN projects p ON ppn.project_id = p.id
                WHERE p.user_id = %s AND pn.merchant_id = %s
                ORDER BY pn.number
            """)
            cursor.execute(query, (current_user.id, current_user.merchant_id))
        
        else:
            cursor.close()
            raise HTTPException(status_code=403, detail="Invalid user role")
        
        rows = cursor.fetchall()
        phone_numbers = [{
            "id": row[0],
            "number": row[1],
            "customer_name": row[2] if row[2] else "N/A"
        } for row in rows]
        
        # Fetch merchant information
        merchant_query = sql.SQL("SELECT id, name FROM merchants WHERE id = %s")
        cursor.execute(merchant_query, (current_user.merchant_id,))
        merchant_row = cursor.fetchone()
        merchant = {"id": merchant_row[0], "name": merchant_row[1]}
        
        cursor.close()
        
        return templates.TemplateResponse("sms_dashboard.html", {
            "request": request,
            "phone_numbers": phone_numbers,
            "merchant": merchant,
            "current_user": current_user
        })
    except Exception as e:
        print(f"Error loading dashboard: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        release_db_connection(connection)

@router.get("/messages/{phone_number_id}", response_class=HTMLResponse)
async def view_messages(request: Request, phone_number_id: int, current_user: User = Depends(get_current_user)):
    sms_service = SMSService()
    messages = sms_service.get_messages(
        merchant_id=current_user.merchant_id,
        phone_number_id=phone_number_id,
        user_id=current_user.id,
        role=current_user.role.value
    )
    
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        
        # Get phone number details
        query = sql.SQL("""
            SELECT pn.number, c.name
            FROM phone_numbers pn
            LEFT JOIN customers c ON pn.customer_id = c.id
            WHERE pn.id = %s AND pn.merchant_id = %s
        """)
        cursor.execute(query, (phone_number_id, current_user.merchant_id))
        row = cursor.fetchone()
        if not row:
            cursor.close()
            raise HTTPException(status_code=404, detail="Phone number not found")
        
        phone_number = {
            "number": row[0],
            "customer_name": row[1] if row[1] else "N/A"
        }
        
        # Fetch merchant information
        merchant_query = sql.SQL("SELECT id, name FROM merchants WHERE id = %s")
        cursor.execute(merchant_query, (current_user.merchant_id,))
        merchant_row = cursor.fetchone()
        merchant = {"id": merchant_row[0], "name": merchant_row[1]}
        
        cursor.close()
        
        return templates.TemplateResponse("sms_detail.html", {
            "request": request,
            "messages": messages,
            "phone_number": phone_number,
            "merchant": merchant,
            "current_user": current_user
        })
    except Exception as e:
        print(f"Error loading messages: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        release_db_connection(connection)

@router.get("/messages/detail/{message_id}", response_class=HTMLResponse)
async def sms_detail_view(request: Request, message_id: int, current_user: User = Depends(get_current_user)):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        
        query = sql.SQL("""
            SELECT sm.id, sm.from_number_id, sm.to_number_id, sm.content, sm.timestamp, sm.status,
                   from_pn.number, from_pn.merchant_id,
                   to_pn.number, to_pn.merchant_id,
                   c_from.name, c_to.name
            FROM sms_messages sm
            JOIN phone_numbers from_pn ON sm.from_number_id = from_pn.id
            JOIN phone_numbers to_pn ON sm.to_number_id = to_pn.id
            LEFT JOIN customers c_from ON from_pn.customer_id = c_from.id
            LEFT JOIN customers c_to ON to_pn.customer_id = c_to.id
            WHERE sm.id = %s
        """)
        cursor.execute(query, (message_id,))
        row = cursor.fetchone()
        if not row:
            cursor.close()
            raise HTTPException(status_code=404, detail="Message not found")
        
        message = {
            "id": row[0],
            "from_number_id": row[1],
            "to_number_id": row[2],
            "content": row[3],
            "timestamp": row[4],
            "status": row[5],
            "from_number": row[6],
            "from_merchant_id": row[7],
            "to_number": row[8],
            "to_merchant_id": row[9],
            "from_customer_name": row[10],
            "to_customer_name": row[11]
        }
        
        # Access Control
        if current_user.role == "Admin":
            pass  # Admin has access to all messages within the merchant
        elif current_user.role == "Operator":
            # Verify if the operator is responsible for either from_number or to_number
            # Fetch project phone numbers
            project_query = sql.SQL("""
                SELECT ppn.phone_number_id
                FROM projects p
                JOIN project_phone_numbers ppn ON p.id = ppn.project_id
                WHERE p.user_id = %s
            """)
            cursor.execute(project_query, (current_user.id,))
            project_phone_ids = [r[0] for r in cursor.fetchall()]
            
            if message["from_number_id"] not in project_phone_ids and message["to_number_id"] not in project_phone_ids:
                cursor.close()
                raise HTTPException(status_code=403, detail="Not authorized to view this message")
        
        else:
            cursor.close()
            raise HTTPException(status_code=403, detail="Invalid user role")
        
        # Fetch merchant information
        merchant_query = sql.SQL("SELECT id, name FROM merchants WHERE id = %s")
        cursor.execute(merchant_query, (current_user.merchant_id,))
        merchant_row = cursor.fetchone()
        merchant = {"id": merchant_row[0], "name": merchant_row[1]}
        
        cursor.close()
        
        return templates.TemplateResponse("sms_detail_view.html", {
            "request": request,
            "message": message,
            "merchant": merchant,
            "current_user": current_user
        })
    except Exception as e:
        print(f"Error loading message detail: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        release_db_connection(connection)