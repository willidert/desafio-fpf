from fastapi import APIRouter, Depends
from src.schemas import productSchema
from typing import List
from sqlalchemy .orm import Session
from src.api.deps import get_db
from src.services import productService

router = APIRouter()

@router.get("/", response_model=List[productSchema.Product])
def get_products(db: Session = Depends(get_db)):
    return productService.get_products(db)
