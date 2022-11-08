from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.db.base_class import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=225), nullable=False)

    products = relationship("Product", back_populates="category")
