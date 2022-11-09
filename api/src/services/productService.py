from typing import List
from sqlalchemy.orm import Session

from src.models.product import Product
from src.schemas import productSchema


def get_products(db: Session, skip=0, limit=100) -> List[productSchema.Product]:
    return db.query(Product).offset(skip).limit(limit).all()
