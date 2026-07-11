from sqlalchemy.orm import Session
from app.models.product_model import Product

class ProductService:
    def get_products(db:Session):
        return db.query(Product).all()
    
    @staticmethod
    def create_product(db:Session,data):
        product = Product(name = data["name"],
        description = data["description"],
        price = data["price"],
        quantity = data["quantity"])
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_product_by_id(db:Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            return product
        return {"message" : "product Not Found"}

    @staticmethod
    def update_product(db:Session, product_id: int, data):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            product.name = data.get("name",product.name)
            product.description = data.get("description",product.description)
            product.price = data.get("price",product.price)
            product.quantity = data.get("quantity",product.quantity)
            db.commit()
            db.refresh(product)
            return product
        return {"message": f"Product {product_id} Not Found"}

    @staticmethod
    def delete_product(db:Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            db.delete(product)
            db.commit()
            return {"message": f"Product {product_id} Deleted"}
        return {"message": f"Product {product_id} Not Found"}

product_service = ProductService()