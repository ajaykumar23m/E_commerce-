from pydantic import BaseModel
from decimal import Decimal 

class OrderCreate(BaseModel):
    user_id : int 
    product_id : int 
    quantity : int 
    total_price : float 

class OrderUpdate(BaseModel):
    user_id : int | None = None
    product_id : int | None = None
    quantity : int | None = None
    total_price : float | None = None 

class OrderResponse(BaseModel):
    id : int 
    user_id : int 
    product_id : int 
    quantity : int
    total_price : float
    class config:
        from_attributes = True 