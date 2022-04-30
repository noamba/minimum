deps:
	echo "installing dependencies" && pip install -r requirements.txt

test:
	echo "running tests" && python -m pytest -v --failed-first --cov-report html --cov=src
