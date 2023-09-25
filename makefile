MANAGE := poetry run python manage.py

install: 
	poetry install

make-migration:
	@$ (MANAGE) makemigrations

migrate: make-migration
	@$ (MANAGE) migrate

build: install migrate

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

test:
	python3 manage.py test

coverage:
	coverage report

run:
	python3 manage.py runserver

makemessages:
	django-admin makemessages -l ru

compilemessages:
	django-admin compilemessages

lint:
	poetry run flake8 task_manager