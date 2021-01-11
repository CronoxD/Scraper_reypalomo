
import requests
from bs4 import BeautifulSoup

# Database
from database.db import get_db

# Models
from database.crud import create_category, create_garment

# Urls
URL = 'https://elreypalomo.com'
URL_CATEGORIES = f'{URL}/collections/mujer-todos-los-productos'


def text_to_price_number(text):
    text = text.replace('$', '')
    text = text.replace('MXN', '')
    text = text.strip()

    return float(text)


def is_active_garment(spans):
    if len(spans) == 0:
        return True

    text = spans[0].text.split()
    if text == 'Sin Inventario':
        return False

    return True


def get_categories():
    """Obtiene todas la categorias"""
    res = requests.get(URL_CATEGORIES)
    soup = BeautifulSoup(res.text, 'html.parser')
    li_items = soup.aside.find_all('li', class_='navigation-dropdown-item')

    for li in li_items:
        try:
            category = create_category({
                'name': li.a.text.strip(),
                'slug': li.a.attrs.get('href', '').strip(),
                'is_active': True,
            })
            print(f'Se guarda la categoria: {category.id} - {category.name } slug: {category.slug}')
        except Exception as e:
            print(f'{e.__class__}')


def scrap_garment_by_category(category):
    """Obtiene toda la ropa por categoria"""
    url = f'{URL}{category.slug}'

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    articles = soup.find_all('article')

    for item in articles:
        price = text_to_price_number(
            item.find_all('span', class_='money')[0].text
        )

        is_active = is_active_garment(
            item.find_all('span', class_='product-item-banner')
        )

        try:
            garment = create_garment({
                'name': item.h4.text.strip(),
                'price': price,
                'image_url': None,
                'is_active': is_active,
                'category_id': category.id,
            })
            print(f'Se guarda la prenda: {garment.id} - {garment.name }')
        except Exception as e:
            print(f'{e.__class__}')
