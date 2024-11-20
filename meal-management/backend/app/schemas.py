# backend/app/schemas.py

from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    balance: float
    is_admin: bool

    class Config:
        orm_mode = True

class MealBase(BaseModel):
    breakfast: bool
    lunch: bool
    dinner: bool

class MealCreate(MealBase):
    pass

class MealResponse(MealBase):
    id: int
    date: datetime
    user_id: int

    class Config:
        orm_mode = True
class LoginForm(BaseModel):
    username: str
    password: str
