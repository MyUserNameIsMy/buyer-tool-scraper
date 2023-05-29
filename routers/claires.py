import json

from fastapi import APIRouter
import requests as _requests
import bs4 as _bs4

router = APIRouter(prefix="/claires", tags=["claires"])

URL = "https://www.claires.com/us/bags/girls-bags/"


@router.get("/")
def parse_claires():
    page = _requests.get(URL)
    soup = _bs4.BeautifulSoup(page.content, 'html.parser')
    raw_products = soup.select('li.grid-tile')
    products = []
    for raw_product in raw_products:
        product_id = raw_product.select_one('div.product-tile').get('data-itemid')
        product_name = raw_product.select_one('div.product-name')
        product_url = raw_product.select_one('a.link-wrap.thumb-link').get('href')
        standard_price = raw_product.select_one('span.product-standard-price')
        sales_price = raw_product.select_one('span.product-sales-price')
        promo_message = raw_product.select_one('div.promotional-message')
        images = []
        front_face = raw_product.select_one('div.card div.front.face img')
        back_face = raw_product.select_one('div.card div.back.face img')
        if not product_id or not product_name or not product_url or not standard_price or not sales_price or not promo_message:
            continue

        product = {'product_id': raw_product.select_one('div.product-tile').get('data-itemid'),
                   'product_name': raw_product.select_one('div.product-name').text,
                   'product_url': raw_product.select_one('a.link-wrap.thumb-link').get('href'),
                   'standard_price': raw_product.select_one('div.product-pricing span.product-standard-price').text,
                   'sales_price': raw_product.select_one('span.product-sales-price').text,
                   'promo_message': raw_product.select_one('div.promotional-message').text,
                   'images': [front_face.get('data-src') if front_face is not None else None,
                              back_face.get('data-src') if back_face is not None else
                              None]}
        products.append(product)

    return json.dumps(products)
