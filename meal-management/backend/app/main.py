# backend/app/main.py

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, init_db
from fastapi.middleware.cors import CORSMiddleware
from auth import authenticate_user, create_access_token, get_current_user, get_current_admin

from typing import List
init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/meals/", response_model=schemas.MealResponse)
def create_meal(user_id: int, meal: schemas.MealCreate, db: Session = Depends(get_db)):
    return crud.create_meal(db=db, meal=meal, user_id=user_id)


# User endpoint for meal statement
@app.get("/users/{user_id}/meal_statement", response_model=List[schemas.MealResponse])
def get_meal_statement(user_id: int, month: int = None, db: Session = Depends(get_db)):
    return crud.get_user_meal_statement(db, user_id=user_id, month=month)

# Admin endpoint for daily or monthly statement
@app.get("/admin/meal_statement", response_model=List[schemas.MealResponse])
def get_admin_statement(daily: bool = True, db: Session = Depends(get_db)):
    return crud.get_admin_meal_statement(db, daily=daily)

# Endpoint to check user balance
@app.get("/users/{user_id}/balance")
def check_balance(user_id: int, db: Session = Depends(get_db)):
    balance = crud.get_user_balance(db, user_id=user_id)
    return {"balance": balance}
# backend/app/main.py




@app.post("/token")
def login_for_access_token(form_data: schemas.LoginForm, db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Secure routes with dependencies
@app.get("/meals/admin", dependencies=[Depends(get_current_admin)])
def get_admin_meal_status():
    # Logic for admin-only meal status route
    pass

