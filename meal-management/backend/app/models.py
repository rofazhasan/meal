# backend/app/models.p

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    balance = Column(Float, default=0.0)
    is_admin = Column(Boolean, default=False)
    meals = relationship("Meal", back_populates="user")

class Meal(Base):
    __tablename__ = 'meals'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, default=datetime.utcnow)
    breakfast = Column(Boolean, default=False)
    lunch = Column(Boolean, default=False)
    dinner = Column(Boolean, default=False)
    cost = Column(Float, default=0.0)  # cost of the meal for that day
    user = relationship("User", back_populates="meals")
