from sqlalchemy.orm import Session

from database import models
from database.db import SessionLocal


def create_garment(data: {}):
    db_garment = models.Garment(
        name=data['name'],
        price=data['price'],
        image_url=data['image_url'],
        is_active=data['is_active'],
        category_id=data['category_id']
    )

    try:
        session = SessionLocal()
        session.add(db_garment)
        session.commit()
        session.refresh(db_garment)
        return db_garment
    finally:
        session.close()
