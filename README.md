# Simple FastAPI Boilerplate

## Requirements

- Python 3.9.13
- PostgreSQL 14
- Fastapi 0.85.0

## Includes

- JWT
- Login / Register
- Make commdans (Makefile)
- `docker-compose.yml` for local
- Separated docker files for local, production and staging under compose folder
- `pre-commit` (https://pre-commit.com/)

## Setup

### with Docker

- Create a `.env` file (you can refer `.env.example` file)
- Run `make up`

### without Docker

- Create python virtual environment and activate it

```bash
~$ python3 -m venv venv && source venv/bin/activate
```

- Install the requirements

```bash
~$ pip install -r requirements.txt
```

- Create a `.env` file and fill it. (you can refer `.env.example` file)
- Start the local server

```bash
~$ uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Pre Commit

Please install a pre-commit to keep the code organized and in the same structure.

Installation ; https://pre-commit.com/#install

# Required packages are:

- pyupgrade
- autoflake
- isort
- black

## API Documentation

FastAPI provides API documentation using OpenAPI technology. <br/>
You can refer below endpoints after run the application.

- Swagger: ``http://localhost:8000/docs``
- ReDoc: ``http://localhost:8000/redoc``
