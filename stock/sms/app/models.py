from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import enum

class UserRole(str, enum.Enum):
    Admin = "Admin"
    Operator = "Operator"

class Merchant(BaseModel):
    id: int
    name: str

class User(BaseModel):
    id: int
    username: str
    role: UserRole
    merchant_id: int

class Project(BaseModel):
    id: int
    name: str
    user_id: int
    phone_numbers: List[int] = []

class PhoneNumber(BaseModel):
    id: int
    merchant_id: int
    number: str
    customer_id: Optional[int] = None

class Customer(BaseModel):
    id: int
    name: str
    phone_number: str

class SMSMessage(BaseModel):
    id: int
    from_number_id: int
    to_number_id: int
    content: str
    timestamp: datetime
    status: str  # e.g., "sent", "received"