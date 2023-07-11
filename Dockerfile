FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN python -m ensurepip --upgrade

#RUN pip install --upgrade pip

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver:8000"]

EXPOSE 8000
