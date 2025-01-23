install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-aws:
	pip install --upgrade pip &&\
		pip install -r requirements-aws.txt

lint:
	pylint --disable=R,C hello.py

format:
	black *.py

test:
	python3 -m pytest -v --cov=hello test_hello.py
