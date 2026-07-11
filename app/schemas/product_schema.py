from pydantic import BaseModel

class ProductCreate(BaseModel):
    name : str 
    description : str
    price : float
    quantity : int
    category_id : int

class ProductUpdate(BaseModel):
    name : str | None = None
    description : str | None = None
    price : float | None = None
    quantity : int | None = None 
    category_id : int | None = None

class ProductResponse(BaseModel):
    id : int 
    name : str
    description : str
    price : float
    quantity : int
    category_id : int

    class config:
        from_attributes = True