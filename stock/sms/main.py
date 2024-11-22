from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import authenticate_user, create_access_token, Token
from app.database import Base, engine
from app.routers import sms
from app.models import Merchant, User, PhoneNumber, Customer, SMSMessage, Project, ProjectPhoneNumber
from fastapi.templating import Jinja2Templates
from app.auth import get_current_user
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2 import sql

Base.metadata.create_all(bind=engine)  # If using ORMs; skip or manage separately with migrations

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# CORS middleware (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include SMS router
app.include_router(sms.router)

# Authentication Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_in_db = authenticate_user(form_data.username, form_data.password)
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user_in_db.id}
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Logout Endpoint (Client-side token handling)
@app.post("/logout")
async def logout():
    # Since JWTs are stateless, logout can be handled client-side by deleting the token
    return {"message": "Logged out successfully"}

@app.get("/")
async def root():
    return {"message": "Hello World"}