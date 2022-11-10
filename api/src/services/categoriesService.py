from typing import List, Optional
from sqlalchemy.orm import Session

from src.models.category import Category
from src.schemas import categorySchema


def get_categories(db: Session, skip=0, limit=100) -> List[categorySchema.Category]:
    return db.query(Category).offset(skip).limit(limit).all()

def get_category_by_id(db: Session, id: int) -> Optional[categorySchema.Category]:
    return db.query(Category).where(Category.id == id)

def create_category(db: Session, category: categorySchema.CategoryCreate) -> categorySchema.Category:
    db_category = Category(category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category: categorySchema.CategoryUpdate, id: int) -> None:
    db.query(Category).filter(Category.id == id).update(category.dict(exclude_unset=True))
    db.commit()

def delete_category(db: Session, id: int) -> None:
    db.query(Category).filter(Category.id == id).delete()
    db.commit()
