
# SQLalchemy
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

# Database
from database.db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    garments = relationship("Garment", back_populates="category")
