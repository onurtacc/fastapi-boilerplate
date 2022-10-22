FROM python:3.9.13-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt-get update && apt-get -y install libpq-dev gcc
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY ./compose/local/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

EXPOSE 8000

ENTRYPOINT ["/entrypoint"]
