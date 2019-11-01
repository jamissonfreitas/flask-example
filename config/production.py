from .default import *
from decouple import config

DEBUG = False

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=config('POSTGRES_USER'),
    pw=config('POSTGRES_PW'),
    url=config('POSTGRES_URL'),
    db=config('POSTGRES_DB')
)
