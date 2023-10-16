FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . ./
