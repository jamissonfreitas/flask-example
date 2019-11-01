# Flask + swagger
- Exemplo de aplicação flask + swagger


# Settings
```
git clone
cd flask-exemple
mkvirtualenv flask-example -p python3
pip install -r requirements.txt
```

# Run app

```
python app.py
```

# Docker run

```
docker build -t flask-example .
docker run -p 8787:8787 flask-example
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