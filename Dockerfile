FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT FLASK_APP=lyrics_fetcher.py flask run --host=0.0.0.0

EXPOSE 5000