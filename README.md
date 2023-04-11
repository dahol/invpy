# Python inventory-app

## Prereqs:

PostgresQL (or replace with sqlite3 in settings.py)

## Packages used (as of 11.04.2023)

```
asgiref==3.6.0
Django==4.1.7
psycopg2-binary==2.9.5
python-dotenv==1.0.0
sqlparse==0.4.3
tzdata==2023.3
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

run docker.sh

```
