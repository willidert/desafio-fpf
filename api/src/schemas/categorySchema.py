from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: Optional[str]

class CategoryCreate(CategoryBase):
    name: str

class CategoryUpdate(CategoryBase):
    pass

class CategoryDBBase(CategoryBase):
    id: int
    name: str

    class Config:
        orm_mode = True

class Category(CategoryDBBase):
    pass

class CategoryInDB(CategoryDBBase):
    pass
