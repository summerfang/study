import os
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from .models import User
from .database import get_db_connection, release_db_connection
from .models import UserRole
import psycopg2
from .database import get_db_connection, release_db_connection

from pydantic import BaseModel

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")  # e.g., "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None

class UserInDB(User):
    hashed_password: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
    
def get_password_hash(password):
    return pwd_context.hash(password)
    
def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        query = sql.SQL("""
            SELECT id, username, hashed_password, role, merchant_id
            FROM users
            WHERE username = %s
        """)
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if not row:
            return None
        user_in_db = UserInDB(
            id=row[0],
            username=row[1],
            hashed_password=row[2],
            role=row[3],
            merchant_id=row[4]
        )
        if not verify_password(password, user_in_db.hashed_password):
            return None
        return user_in_db
    except Exception as e:
        print(f"Error during authentication: {e}")
        return None
    finally:
        release_db_connection(connection)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        query = sql.SQL("""
            SELECT id, username, role, merchant_id
            FROM users
            WHERE id = %s
        """)
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()
        if not row:
            raise credentials_exception
        user = User(
            id=row[0],
            username=row[1],
            role=row[2],
            merchant_id=row[3]
        )
        cursor.close()
        return user
    except Exception as e:
        print(f"Error fetching current user: {e}")
        raise credentials_exception
    finally:
        release_db_connection(connection)