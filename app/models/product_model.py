from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))

    name = Column(String(100), nullable=False)
    description = Column(String(300))
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)

    category = relationship("Category", back_populates="products")
    orders = relationship("Order", back_populates="product")