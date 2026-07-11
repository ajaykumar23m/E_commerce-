from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.order_schema import OrderCreate, OrderUpdate

from app.services.order_service import (
    get_orders as service_get_orders,
    create_order as service_create_order,
    get_order as service_get_order,
    update_order as service_update_order,
    delete_order as service_delete_order
)

order_router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@order_router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return service_get_orders(db)


@order_router.post("/")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return service_create_order(db, order.model_dump())


@order_router.get("/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    return service_get_order(db, order_id)


@order_router.put("/{order_id}")
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    return service_update_order(db, order_id, order.model_dump())


@order_router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return service_delete_order(db, order_id)