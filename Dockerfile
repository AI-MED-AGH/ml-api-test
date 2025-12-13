FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./mlapi_server.py /code/mlapi_server.py


CMD ["python", "mlapi_server.py"]
