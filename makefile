install: 
	poetry install

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

build: install migrate

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

test:
	poetry run python3 manage.py test

coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/*

run:
	poetry run python3 manage.py runserver

makemessages:
	poetry run django-admin makemessages -l ru

compilemessages:
	poetry run django-admin compilemessages

lint:
	poetry run flake8 task_manager