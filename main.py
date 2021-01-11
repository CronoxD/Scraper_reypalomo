
from database.db import Base, engine, SessionLocal
from database import models
import time

# Scraper
from scraper import get_categories, scrap_garment_by_category


if __name__ == "__main__":
    # Create database
    Base.metadata.create_all(bind=engine)

    get_categories()
    try:
        session = SessionLocal()
        categories = session.query(models.Category).all()

        for category in categories:
            time.sleep(11)
            scrap_garment_by_category(category)
            print('Esperando 11 segundos...')
    except Exception as e:
        print(e)
    finally:
        session.close()
