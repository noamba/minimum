deps:
	echo "installing dependencies" && poetry install

test:
	echo "running unit tests" && poetry run python -m pytest -v --failed-first --cov-report html --cov=src
