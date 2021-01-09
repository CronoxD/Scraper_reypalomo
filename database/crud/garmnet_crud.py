from sqlalchemy.orm import Session

from database import models


def create_garment(db: Session, data: {}):
    db_garment = models.Garment(
        name=data['name'],
        price=data['price'],
        image_url=data['image_url'],
        is_active=data['is_active'],
        category_id=data['category_id']
    )

    db.add(db_garment)
    db.commit()
    db.refresh(db_garment)
    return db_garment
