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

test:
	pytest $$(find ./src -name '*.py')

black:
	black --config .flake8 $$(find ./src -name '*.py') --check

isort:
	isort --profile="black" $$(find ./src -name '*.py') --check-only

all: black isort tests

# ---------------------------------------------------------------------------- #
# document
# ---------------------------------------------------------------------------- #

build-docs:
	pushd $$PROJECT_DIR/docs &&\
		sphinx-apidoc -f -o source/ ../dsc &&\
		make html &&\
		popd

# ---------------------------------------------------------------------------- #
# release
# ---------------------------------------------------------------------------- #

clean-dist:
	if [ -d $$PROJECT_DIR/dist ]; then rm -rf $$PROJECT_DIR/dist; fi
	if [ -d $$PROJECT_DIR/data_science_common.egg-info ]; then rm -rf $$PROJECT_DIR/data_science_common.egg-info; fi

build-dist: clean-dist
	python -m build

deploy-test-pypi: build-dist
	twine upload --verbose --repository testpypi dist/*

deploy-pypi: build-dist
	twine upload --verbose dist/*
