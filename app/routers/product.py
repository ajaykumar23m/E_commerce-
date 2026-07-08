from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.services.product_service import ProductService

product_router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@product_router.get("/")
def get_products(db: Session = Depends(get_db)):
    return ProductService.get_products(db)

@product_router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db, product.model_dump())

@product_router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService.get_product_by_id(db, product_id)

@product_router.put("/{product_id}")
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return ProductService.update_product(db, product_id, product.model_dump())

@product_router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService.delete_product(db, product_id)