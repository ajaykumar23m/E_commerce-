from sqlalchemy.orm import Session
from app.models.category_model import Category


def get_categories(db: Session):
    return db.query(Category).all()


def create_category(db: Session, data):
    category = Category(
        name=data["name"],
        description=data["description"]
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def update_category(db: Session, category_id: int, data):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        return {"message": "Category Not Found"}

    category.name = data["name"]
    category.description = data["description"]

    db.commit()
    db.refresh(category)

    return category


def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        return {"message": "Category Not Found"}

    db.delete(category)
    db.commit()

    return {"message": "Category Deleted Successfully"}