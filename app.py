#!/usr/bin/env python
from flask import Flask
from safrs import SAFRSBase, SAFRSAPI
from example.products.models import Product
from config import db
from decouple import config


app = Flask("Products API")


def create_api(app):
    api = SAFRSAPI(
        app,
        debug=config('DEBUG'),
        host=config('HOST'),
        port=config('PORT'),
        prefix=''
    )
    api.expose_object(Product)
    print("Starting API: http://{}:{}/{}".format(
        config('HOST'), config('PORT'), ''))


def create_app():
    app.config.from_object(config('FLASK_CONFIG'))
    db.init_app(app)
    with app.app_context():
        db.create_all()
        create_api(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host=config('HOST'),
        port=config('PORT')
    )
