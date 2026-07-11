from fastapi import FastAPI
from app.database import Base, engine

from app.models.product_model import Product
from app.models.category_model import Category
from app.models.user_model import User
from app.models.order_model import Order


from app.routers.product import product_router 
from app.routers.category import category_router 
from app.routers.user import user_router
from app.routers.order import order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    version="1.0.0"
)

app.include_router(product_router)
app.include_router(category_router)
app.include_router(user_router)
app.include_router(order_router)
