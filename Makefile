# ---------------------------------------------------------------------------- #
# setup
# ---------------------------------------------------------------------------- #

setup:
	pyenv install --skip-existing 3.10.2 &&\
		pyenv uninstall -f dsc &&\
		pyenv virtualenv --force 3.10.2 dsc &&\
		pyenv local dsc &&\
		pip install --upgrade pip &&\
		pip install -r requirements.txt

install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt

# ---------------------------------------------------------------------------- #
# test
# ---------------------------------------------------------------------------- #

#backend-test:
#	pytest --tb=short $$(find ./services/search/* -name '*.py')
#
#flake8:
#	flake8 --config .flake8 $$(find ./services/search/* -name '*.py')
#
#black:
#	black $$(find ./services/search/* -name '*.py') --check
#
#isort:
#	isort --profile="black" $$(find ./services/search/* -name '*.py') --check-only
#
#all: flake8 black isort backend-test
