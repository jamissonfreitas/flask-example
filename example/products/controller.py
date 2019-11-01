from flask import jsonify
from .models import Product
from config import db


def get_products(product_id=None):
    if product_id:
        product = db.session.query(Product).filter_by(id = product_id).one()
        return jsonify(product=product.serialize)
    else:
        products = db.session.query(Product).all()
        return jsonify(products=[p.serialize for p in products])


def create_product(nome, description):
    newProduct = Product(nome=nome, description=description)
    db.session.add(newProduct)
    db.session.commit()
    return jsonify(Product=newProduct.serialize)
