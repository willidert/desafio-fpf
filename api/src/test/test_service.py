from sqlalchemy.orm import Session
from decimal import Decimal
from pytest import approx

from src.schemas import productSchema
from src.services import productService
from src.test.utils import generate_random_datetime, generate_random_str, generate_random_float

def test_get_products(db: Session) -> None:
    products = productService.get_products(db)
    assert len(products) == 0
    assert type(products) == list

def test_create_product(db: Session) -> None:
    category = generate_random_str()
    description = generate_random_str()
    price = generate_random_float()
    purchase_date = generate_random_datetime()
    
    product = productSchema.ProductCreate(category=category, description=description, price=price, purchase_date=purchase_date)
    product_created = productService.create_product(db, product)

    assert product_created.category == category
    assert product_created.price == approx(Decimal.from_float(price)) # limitação do banco de dados?
    assert product_created.description == description
    assert product_created.purchase_date == purchase_date

def test_get_product_by_id(db: Session) -> None:
    category = generate_random_str()
    description = generate_random_str()
    price = generate_random_float()
    purchase_date = generate_random_datetime()
    
    product = productSchema.ProductCreate(category=category, description=description, price=price, purchase_date=purchase_date)
    product_created = productService.create_product(db, product)

    stored_product = productService.get_product_by_id(db, product_created.id)

    assert stored_product
    assert stored_product.id == product_created.id
    assert stored_product.category == product_created.category
    assert stored_product.price == product_created.price
    assert stored_product.description == product_created.description
    assert stored_product.purchase_date == product_created.purchase_date

def test_update_product(db: Session) -> None:
    category = generate_random_str()
    description = generate_random_str()
    price = generate_random_float()
    purchase_date = generate_random_datetime()
    
    product = productSchema.ProductCreate(category=category, description=description, price=price, purchase_date=purchase_date)
    product_created = productService.create_product(db, product)

    new_description = generate_random_str()
    product_update = productSchema.ProductUpdate(category=category, description=new_description, price=price, purchase_date=purchase_date)

    product_updated = productService.update_product(db, product_update, product_created.id)

    assert product_updated
    assert product_updated.description == new_description
    assert product_updated.category == product_created.category

def test_delete_product(db: Session) -> None:
    category = generate_random_str()
    description = generate_random_str()
    price = generate_random_float()
    purchase_date = generate_random_datetime()
    
    product = productSchema.ProductCreate(category=category, description=description, price=price, purchase_date=purchase_date)
    product_created = productService.create_product(db, product)

    product_deleted = productService.delete_product(db, product_created.id)
    assert product_deleted
    assert product_deleted.id == product_created.id
    assert product_deleted.category == product_created.category
    assert product_deleted.description == product_created.description
    assert product_deleted.price == product_created.price
    assert product_deleted.purchase_date == product_created.purchase_date
