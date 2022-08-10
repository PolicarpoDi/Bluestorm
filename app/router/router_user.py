from fastapi import APIRouter, Depends, HTTPException, status
from connection.database import SessionLocal
from model.models import UserModel
from fastapi.responses import JSONResponse
from controller.crud import get_users, create_user
from sqlalchemy.orm import Session
from typing import List


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


# /user/create [POST] { .. }
@router.post("/users/create", status_code=status.HTTP_201_CREATED, response_model=UserModel)
def users_create(user: UserModel, db: Session = Depends(get_db)):
    #user.PASSWORD = hash_provider.create_hash(user.PASSWORD)
    user_create = create_user(user, db)
    return JSONResponse(content=user_create)


# /users/ [GET] { .. }
@router.get("/users/", status_code=status.HTTP_200_OK, response_model=List[UserModel])
def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    if not users:
        raise HTTPException(status_code=404, detail='User not found!')
    return JSONResponse(content=users)