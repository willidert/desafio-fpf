from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    description: Optional[str]
    price: Optional[float]
    purchase_date: Optional[datetime]

class ProductCreate(ProductBase):
    description: str
    price: float
    purchase_date: datetime

class ProductUpdate(ProductBase):
    pass

class ProductInDBBase(ProductBase):
    description: str
    price: float
    purchase_date: datetime

    class Config:
        orm_mode = True

class Product(ProductInDBBase):
    pass

class ProductInDB(ProductInDBBase):
    pass
