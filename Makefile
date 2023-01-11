run:
	@pipenv run python src/script.py

install:
	@pipenv install --skip-lock

lint:
	@pipenv run black .
	@pipenv run isort .