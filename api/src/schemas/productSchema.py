from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    description: Optional[str]
    price: Optional[float]
    purchase_date: Optional[datetime]
    category: Optional[str]

class ProductCreate(ProductBase):
    description: str
    price: float
    purchase_date: datetime
    category: str

class ProductUpdate(ProductBase):
    pass

class ProductInDBBase(ProductBase):
    id: int
    description: str
    price: float
    purchase_date: datetime
    category: str

    class Config:
        orm_mode = True

class Product(ProductInDBBase):
    pass

class ProductInDB(ProductInDBBase):
    pass
