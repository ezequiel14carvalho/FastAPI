from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

# Use bcrypt_sha256 to avoid bcrypt's 72-byte password limit and
# backend compatibility issues with passlib.
bcrypt_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

from order_routes import order_router
from auth_routes import auth_router

app.include_router(auth_router)
app.include_router(order_router)
