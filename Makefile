
# target: run - Runs a dev server on localhost:8000
run:
	python manage.py runserver

app:
	python manage.py startapp $$name

# target: deps - install dependencies from requirements file
prod_deps:
	pip install -r requirements.txt
	cd src && pip install -e .
	pip install -e .

dev_deps:
	pip install -r dev-requirements.txt
	pre-commit install
	mkdir -p media

deps: dev_deps prod_deps


# target: migrate - migrate the database
migrate:
	python manage.py makemigrations
	python manage.py migrate

adminuser:
	python manage.py createsuperuser