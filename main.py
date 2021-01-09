
from database.db import Base, engine

# Scraper
from scraper import get_categories


if __name__ == "__main__":
    # Create database
    Base.metadata.create_all(bind=engine)

    get_categories()
