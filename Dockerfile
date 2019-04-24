FROM python:latest

COPY . /code

WORKDIR /code

CMD ["python", "main.py"]

