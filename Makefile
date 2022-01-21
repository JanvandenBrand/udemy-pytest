setup:
	python3 -m venv ~/.udemy-pytest
	#source ~/.udemy-pytest/bin/activate
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	#hadolint Dockerfile #uncomment to explore linting Dockerfiles
	pylint --disable=R,C app.py

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

