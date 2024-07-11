all:
	poetry run pylint pygleton/
	poetry run ruff check pygleton/
	poetry run black -l 79 --check pygleton/
	poetry run isort -c pygleton/
	poetry run pylint tests/
	poetry run ruff check tests/
	poetry run black -l 79 --check tests/
	poetry run isort -c tests/
	poetry run pytest --cov=. --cov-report=html --cov-fail-under=100
