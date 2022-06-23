from typing import List

import pymongo
from bson import ObjectId

client = pymongo.MongoClient()
db = client['productsdb']
products = db['products']


def get_products(filter: dict) -> List[dict]:
    return list(products.find(filter))


def add_product(product_data: dict) -> dict:
    product = products.insert_one(product_data)
    new_product = products.find_one({'_id': product.inserted_id})
    return new_product


def get_product(product_id: str) -> dict:
    product = products.find_one({'_id': ObjectId(product_id)})
    return product
