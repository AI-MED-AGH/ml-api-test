FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y binutils gcc g++

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir .

COPY . /app

RUN pyinstaller mlapi_server.spec --noconfirm
