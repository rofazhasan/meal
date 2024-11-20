# backend/app/crud.py

from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime, timedelta

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_meal(db: Session, meal: schemas.MealCreate, user_id: int):
    db_meal = models.Meal(**meal.dict(), user_id=user_id, date=datetime.now())
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def get_user_balance(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user.balance

def get_user_meal_statement(db: Session, user_id: int, month: int = None):
    query = db.query(models.Meal).filter(models.Meal.user_id == user_id)
    if month:
        query = query.filter(models.Meal.date.between(
            datetime(datetime.now().year, month, 1),
            datetime(datetime.now().year, month, 1) + timedelta(days=30)
        ))
    return query.all()

def get_admin_meal_statement(db: Session, daily: bool = True):
    if daily:
        date = datetime.now().date()
        return db.query(models.Meal).filter(models.Meal.date == date).all()
    else:
        month_start = datetime(datetime.now().year, datetime.now().month, 1)
        month_end = month_start + timedelta(days=30)
        return db.query(models.Meal).filter(models.Meal.date.between(month_start, month_end)).all()

