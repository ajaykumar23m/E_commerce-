from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.category_schema import CategoryCreate, CategoryUpdate
from app.services.category_service import get_categories, create_category, get_category, update_category, delete_category

category_router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@category_router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return CategoryService.get_categories(db)

@category_router.post("/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return CategoryService.create_category(db, category.model_dump())

@category_router.get("/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    return CategoryService.get_category(db, category_id)

@category_router.put("/{category_id}")
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    return CategoryService.update_category(db, category_id, category.model_dump())

@category_router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return CategoryService.delete_category(db, category_id)