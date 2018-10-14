FROM python:3.6-slim

COPY . .
RUN pip install -r requirements/prod.txt

EXPOSE 8080

ENTRYPOINT python ./application.py

