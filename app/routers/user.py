from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user_schema import UserCreate, UserUpdate
from app.services.user_service import (
    get_users as service_get_users,
    create_user as service_create_user,
    get_user as service_get_user,
    update_user as service_update_user,
    delete_user as service_delete_user
)

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("/")
def get_users(db: Session = Depends(get_db)):
    return service_get_users(db)

@user_router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return service_create_user(db, user.model_dump())

@user_router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return service_get_user(db, user_id)

@user_router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return service_update_user(db, user_id, user.model_dump())

@user_router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return service_delete_user(db, user_id)