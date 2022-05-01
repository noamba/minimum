deps:
	echo "installing dependencies" && \
	python3 -m pip install -r requirements.txt && \
	python3 -m pip install -r requirements-dev.txt

test:
	echo "running tests" && \
	python3 -m pytest -v --failed-first --cov-report html --cov=minimum
