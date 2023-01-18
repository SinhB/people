# people

### Description

Backend application made with Python's FastAPI framework and Hexagonal Architecture.
It expose 4 endpoints:
- Create multiple people
- Get average age of people by country
- Get number of people from each country
- Get the gender repartition for a given country


### Overview

- Language: Python3.10
- Web Framework: FastAPI
- Production web server: Uvicorn
- Relational database: SQLite
- Relational ORM: SQLAlchemy
- Data parsing and validation: Pydantic
- Testing: Pytest, Starlette
- Linter: Flake8
- Formatter: Black

### Installation

Install requirements:
`pip install -r requirements.txt`

Run the app:
`uvicorn people.main:app`

Run tests:
`pytest -vv`

Swagger:
`http://<hostname>:8000/docs`

#### Disclaimer

This is not a production code. The purpose of this code is to test hexagonal architecture with minimalist FastAPI application. Technical choices were made that may not prioritize security.

### Walkthrough

You can found my notebook [here](/walkthrough)
