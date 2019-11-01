from .default import *
from decouple import config


SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')