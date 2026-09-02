from datetime import datetime
from decimal import Decimal
from typing import List
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ExpenseBase(BaseModel):
    value: Decimal
    description: str = Field(max_length=200)
    datetime: datetime

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    user_id: int
           
    model_config = ConfigDict(from_attributes=True)
    

class UserBase(BaseModel):
    username: str = Field(max_length=50)
    email: EmailStr = Field(max_length=255)

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    expenses: List[ExpenseResponse] = []
        
    model_config = ConfigDict(from_attributes=True)