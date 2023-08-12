FROM python:3.11.4-alpine3.18

MAINTAINER Andrey Shaikin <kiwibon@yandex.ru>

ENV PROJECT_DIR=/app

USER root

WORKDIR $PROJECT_DIR

RUN true \
    && apk update \
    && apk add --no-cache \
    make

COPY requirements requirements
RUN python3 -m pip install --no-cache-dir -r requirements/main.txt -r requirements/dev.txt

COPY app.py .flake8 alembic.ini  Makefile ./
COPY conf conf
COPY apps apps
COPY db db
COPY utils utils

EXPOSE 80
CMD ["make", "run_server"]
