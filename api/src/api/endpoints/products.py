from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas import productSchema
from typing import List, Optional
from sqlalchemy .orm import Session
from src.api.deps import get_db
from src.services import productService

router = APIRouter()

@router.get("/", response_model=List[productSchema.Product])
def get_products(db: Session = Depends(get_db)):
    return productService.get_products(db)


@router.get('/{id}', response_model=Optional[productSchema.Product])
def get_product_by_id(db: Session = Depends(get_db)):
    product = productService.get_product_by_id(db, id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found.')
    return product

@router.post('/', response_model=productSchema.Product, status_code=status.HTTP_201_CREATED)
def create_product(product: productSchema.ProductCreate, db: Session = Depends(get_db)):
    return productService.create_product(db, product)

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def update_product(product: productSchema.ProductUpdate, id: int, db: Session = Depends(get_db)):
    product = productService.get_product_by_id(db, id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found.')
    return productService.update_product(db, product, id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):
    product = productService.get_product_by_id(db, id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found.')
    productService.delete_product(db, id)
