from sqlalchemy.orm import Session
from app.models.order_model import Order


def get_orders(db: Session):
    return db.query(Order).all()


def create_order(db: Session, data):
    order = Order(
        user_id=data["user_id"],
        product_id=data["product_id"],
        quantity=data["quantity"],
        total_price=data["total_price"]
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def update_order(db: Session, order_id: int, data):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return {"message": "Order Not Found"}

    order.user_id = data["user_id"]
    order.product_id = data["product_id"]
    order.quantity = data["quantity"]
    order.total_price = data["total_price"]

    db.commit()
    db.refresh(order)

    return order


def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return {"message": "Order Not Found"}

    db.delete(order)
    db.commit()

    return {"message": "Order Deleted Successfully"}