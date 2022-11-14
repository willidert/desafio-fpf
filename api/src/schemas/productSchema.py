from datetime import datetime
from pydantic import BaseModel, constr, condecimal
from typing import Optional

class ProductBase(BaseModel):
    description: Optional[str]
    price: Optional[condecimal(ge=0)]
    purchase_date: Optional[datetime]
    category: Optional[str]

class ProductCreate(ProductBase):
    description: constr(max_length=225)
    price: condecimal(ge=0)
    purchase_date: datetime
    category: constr(max_length=225)

class ProductUpdate(ProductBase):
    pass

class ProductInDBBase(ProductBase):
    id: int
    description: constr(max_length=225)
    price: condecimal(ge=0)
    purchase_date: datetime
    category: constr(max_length=225)

    class Config:
        orm_mode = True

class Product(ProductInDBBase):
    pass

class ProductInDB(ProductInDBBase):
    pass
