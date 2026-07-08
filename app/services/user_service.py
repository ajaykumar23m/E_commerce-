from sqlalchemy.orm import Session
from app.models.user_model import User


def get_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, data):
    user = User(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        phone=data["phone"],
        address=data["address"]
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, data):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"message": "User Not Found"}

    user.first_name = data["first_name"]
    user.last_name = data["last_name"]
    user.email = data["email"]
    user.phone = data["phone"]
    user.address = data["address"]

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"message": "User Not Found"}

    db.delete(user)
    db.commit()

    return {"message": "User Deleted Successfully"}