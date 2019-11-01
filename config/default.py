from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
