from typing import List
from sqlalchemy.orm import Session

from src.models.category import Category
from src.schemas import categorySchema


def get_categories(db: Session, skip=0, limit=100) -> List[categorySchema.Category]:
    return db.query(Category).offset(skip).limit(limit).all()
