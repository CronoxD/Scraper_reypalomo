
# SQLalchemy
from sqlalchemy import (
    Boolean, Column, ForeignKey,
    Integer, String, Float
)
from sqlalchemy.orm import relationship

# Database
from database.db import Base

# Models
from database.models import Category


class Garment(Base):
    __tablename__ = "garments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Float)
    image_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    category = relationship("Category", back_populates="garments")
    category_id = Column(Integer, ForeignKey("categories.id"))
