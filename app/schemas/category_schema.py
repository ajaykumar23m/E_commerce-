from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name : str

class CategoryUpdate(BaseModel):
    name : str | None = None 

class CategoryResponse(BaseModel):
    id : int 
    name : str
    class config:
        from_attributes = True 