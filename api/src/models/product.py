from sqlalchemy import Column, String, DateTime, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base_class import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    purchase_date = Column(DateTime(timezone=True), nullable=False)
    price = Column(Float(precision=2, asdecimal=True), nullable=False)
    description = Column(String(length=225), nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")
