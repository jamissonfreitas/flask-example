FROM python:3.6
MAINTAINER James "consultorjamissonfreitas@gmail.com"

COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
