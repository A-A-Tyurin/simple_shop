from http import HTTPStatus
from typing import List

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder

import database as db
import utils
from .models import Product

app = FastAPI()


@app.get('/')
def get_status():
    return {'status': 'running'}


@app.get('/product/', response_model=List[Product])
def get_products_data(request: Request):
    filter = utils.get_filter(request.query_params)
    return db.get_products(filter)


@app.post('/product/', status_code=HTTPStatus.CREATED)
def add_product_data(product: Product):
    new_product = db.add_product(jsonable_encoder(product))
    return {'ID': str(new_product['_id'])}


@app.get('/product/{product_id}/', response_model=Product)
def get_product_data(product_id: str):
    return db.get_product(product_id)
