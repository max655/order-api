from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class OrderCreate(BaseModel):
    title: str
    description: str


class OrderUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class OrderResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime


class Config:
    orm_mode = True
