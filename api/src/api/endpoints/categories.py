from fastapi import APIRouter, Depends
from src.schemas import categorySchema
from typing import List
from sqlalchemy .orm import Session
from src.api.deps import get_db
from src.services import categoriesService

router = APIRouter()

@router.get("/", response_model=List[categorySchema.Category])
def get_categories(db: Session = Depends(get_db)):
    return categoriesService.get_categories(db)
