from sqlalchemy.orm import Session

from database import models
from database.db import SessionLocal


def create_category(data: {}):
    db_category = models.Category(
        name=data['name'],
        slug=data['slug'],
        is_active=data['is_active']
    )

    try:
        session = SessionLocal()
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
        return db_category
    finally:
        session.close()
