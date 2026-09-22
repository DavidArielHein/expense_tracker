from datetime import datetime
from decimal import Decimal
from typing import List
from sqlalchemy import ForeignKey, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class UserDB(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str]
    
    expenses: Mapped[List['ExpenseDB']] = relationship(back_populates='user')


class ExpenseDB(Base):
    __tablename__ = "expenses"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    value: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    description: Mapped[str] = mapped_column(String(200))
    datetime: Mapped[datetime]
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    user: Mapped[UserDB] = relationship(back_populates='expenses')
    
    