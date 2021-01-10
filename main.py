
from database.db import Base, engine, SessionLocal
from database import models

# Scraper
from scraper import get_categories, scrap_garment_by_category


if __name__ == "__main__":
    # Create database
    Base.metadata.create_all(bind=engine)

    # get_categories()
    try:
        session = SessionLocal()
        category = session.query(models.Category).first()
        scrap_garment_by_category(category)
    finally:
        pass
