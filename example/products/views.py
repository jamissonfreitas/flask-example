from flask import Flask, Blueprint, request
from .controller import *

product_api = Blueprint('product_api', __name__)


@product_api.route('/')
@product_api.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return get_products()
    elif request.method == 'POST':
        name = request.args.get('name', '')
        description = request.args.get('description', '')
        return create_product(name, description)
