deps:
	echo "installing dependencies" && \
	python -m pip install -r requirements.txt && \
	python -m pip install -r requirements-dev.txt

test:
	echo "running tests" && \
	python -m pytest -v --failed-first --cov-report html --cov=minimum
