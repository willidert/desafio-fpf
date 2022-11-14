from fastapi.encoders import jsonable_encoder
from typing import List, Optional
from sqlalchemy.orm import Session

from src.models.product import Product
from src.schemas import productSchema


def get_products(db: Session, skip=0, limit=100) -> List[productSchema.Product]:
    return db.query(Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, id: int) -> Optional[productSchema.Product]:
    return db.query(Product).where(Product.id == id).first()

def create_product(db: Session, product: productSchema.ProductCreate) -> productSchema.Product:
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, update_data: productSchema.ProductUpdate, id: int) -> productSchema.Product:
    db.query(Product).filter(Product.id == id).update(update_data.dict())
    db.commit()
    return db.query(Product).filter(Product.id == id).first()

def delete_product(db: Session, id: int) -> productSchema.Product:
    product = db.query(Product).filter(Product.id == id).first()
    db.query(Product).filter(Product.id == id).delete()
    db.commit()
    return product
