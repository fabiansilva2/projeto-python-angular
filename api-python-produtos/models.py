from sqlalchemy import Column, Integer, String, Float

from database import Base

class Product(Base):
    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(60), nullable=False)
    category: str = Column(String(128), nullable=False)
    price: float = Column(Float, nullable=False)
    serie: int = Column(Integer, nullable=False)
