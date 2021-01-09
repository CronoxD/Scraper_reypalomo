
import requests
from bs4 import BeautifulSoup

# Database
from database.db import get_db

# Models
from database.crud import create_category

# Urls
URL = 'https://elreypalomo.com'
URL_CATEGORIES = f'{URL}/collections/mujer-todos-los-productos'


def get_categories():
    url = f'{URL}/collections/mujer-todos-los-productos'

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    li_items = soup.aside.find_all('li', class_='navigation-dropdown-item')

    for li in li_items:
        create_category({
            'name': li.a.text.strip(),
            'slug': li.a.attrs.get('href', '').strip(),
            'is_active': True,
        })
