FROM python:3.6-slim

COPY . .
RUN pip install -r requirements/dev.txt

EXPOSE 8080

ENTRYPOINT python ./application.py

