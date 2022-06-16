# ---------------------------------------------------------------------------- #
# setup
# ---------------------------------------------------------------------------- #

python_version = 3.10.4
python_env = dsc3104

setup:
	pyenv install --skip-existing $(python_version) &&\
		pyenv uninstall -f $(python_env) &&\
		pyenv virtualenv --force $(python_version) $(python_env) &&\
		pyenv local $(python_env) &&\
		pip install --upgrade pip &&\
		pip install -r requirements.txt

install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt

# ---------------------------------------------------------------------------- #
# test
# ---------------------------------------------------------------------------- #

pytest:
	pytest $$(find ./dsc -name '*.py')

black:
	black --config .flake8 $$(find ./dsc -name '*.py') --check

isort:
	isort --profile="black" $$(find ./dsc -name '*.py') --check-only

mypy:
	mypy --ignore-missing-imports --show-error-codes $$(find ./dsc -name '*.py')

test: black isort mypy pytest

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
