FROM python:3.6-slim

ENV SERVICE_VERSION 0.3

COPY . .

RUN pip install -r requirements/prod.txt

EXPOSE 8080

ENTRYPOINT python app/app.py

