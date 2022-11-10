from typing import List, Optional
from sqlalchemy.orm import Session

from src.models.product import Product
from src.schemas import productSchema


def get_products(db: Session, skip=0, limit=100) -> List[productSchema.Product]:
    return db.query(Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, id: int) -> Optional[productSchema.Product]:
    return db.query(Product).where(Product.id == id)

def create_product(db: Session, product: productSchema.ProductCreate) -> productSchema.Product:
    db_product = Product(product.dict)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product: productSchema.ProductUpdate, id: int) -> None:
    db.query(Product).filter(Product.id == id).update(product.dict(exclude_unset=True))
    db.commit()

def delete_product(db: Session, id: int) -> None:
    db.query(Product).filter(Product.id == id).delete()
    db.commit()
