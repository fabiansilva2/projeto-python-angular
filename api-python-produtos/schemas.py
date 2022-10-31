from unicodedata import category
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    category: str
    price: float
    serie: int

class ProductRequest(ProductBase):
    ...

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
