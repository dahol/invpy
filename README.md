# Python inventory-app

## Prereqs:

PostgresQL (or replace with sqlite3 in settings.py)

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

### Build scipt

## How to run

- Kubernetes

  - Build.sh

    - Arguments:
      - `-b true` to build
      - `-p true` to push
      - ex: `sudo ./build.sh -b true -p true`

  - Deploy.sh

    - Arguments:
      - `-u username`
      - `-p password`
      - `-h host`
      - `-d database`
      - `-p port`

- Docker compose (maybe tba)
