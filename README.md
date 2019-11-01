# Flask + swagger
- Exemplo de aplicação flask + swagger


# Settings
```
git clone
cd flask-exemple
```

# Run app

```
mkvirtualenv flask-example -p python3
pip install -r requirements.txt
python app.py
```

# Docker run

```
docker-compose up
```

## Env format
```
DEBUG=False
HOST=0.0.0.0
PORT=8787
FLASK_ENV=development
FLASK_CONFIG=config.development
SECRET_KEY=
POSTGRES_URL=
POSTGRES_USER=
POSTGRES_PW=
POSTGRES_DB=
```