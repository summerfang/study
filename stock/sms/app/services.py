from typing import List
from psycopg2 import sql
from .models import SMSMessage
from .database import get_db_connection, release_db_connection

class SMSService:
    def get_messages(self, merchant_id: int, phone_number_id: int, user_id: int, role: str) -> List[SMSMessage]:
        connection = get_db_connection()
        try:
            cursor = connection.cursor()
            
            if role == "Admin":
                query = sql.SQL("""
                    SELECT id, from_number_id, to_number_id, content, timestamp, status
                    FROM sms_messages
                    WHERE (from_number_id = %s OR to_number_id = %s)
                    ORDER BY timestamp DESC
                """)
                cursor.execute(query, (phone_number_id, phone_number_id))
            
            elif role == "Operator":
                # Assuming there's a table 'project_phone_numbers' linking projects and phone numbers
                # and 'projects' table linking users to projects
                query = sql.SQL("""
                    SELECT sm.id, sm.from_number_id, sm.to_number_id, sm.content, sm.timestamp, sm.status
                    FROM sms_messages sm
                    JOIN project_phone_numbers ppn ON sm.from_number_id = ppn.phone_number_id OR sm.to_number_id = ppn.phone_number_id
                    JOIN projects p ON ppn.project_id = p.id
                    WHERE p.user_id = %s AND (sm.from_number_id = %s OR sm.to_number_id = %s)
                    ORDER BY sm.timestamp DESC
                """)
                cursor.execute(query, (user_id, phone_number_id, phone_number_id))
            
            else:
                return []
            
            rows = cursor.fetchall()
            messages = [SMSMessage(
                id=row[0],
                from_number_id=row[1],
                to_number_id=row[2],
                content=row[3],
                timestamp=row[4],
                status=row[5]
            ) for row in rows]
            
            cursor.close()
            return messages
        except Exception as e:
            print(f"Error fetching messages: {e}")
            return []
        finally:
            release_db_connection(connection)