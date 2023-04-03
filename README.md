# Python inventory-app

## Prereqs:

PostgresQL (or replace with sqlite3 in settings.py)

## Packages used

```
asgiref
Django
psycopg2
python-dotenv
sqlparse
tzdata
```

## How to use

### Local

```

git clone https://github.com/dahol/invpy

cd invpy/

python -m venv .

.\Scripts\activate.ps1

pip install --upgrade pip / python.exe -m pip install --upgrade pip

pip freeze > .\requirements.txt

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```

### Docker

```

git clone https://github.com/dahol/invpy

cd invpy/

pip freeze > .\requirements.txt

run docker.ps1

```
