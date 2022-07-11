.PHONY: help, setup, install, pytest, black, isort, mypy, test, clean-docs, clean-dist, deploy-pypi, deploy-test-pypi

# ---------------------------------------------------------------------------- #

python_version = 3.10.5
python_env = dsc3105
package_name = data_science_common
dsc_version=$$(python -c "import dsc; print(dsc.get_version())")

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'

# ---------------------------------------------------------------------------- #
# devoloper python setup
# ---------------------------------------------------------------------------- #

setup:   ## setup python virtual environment
	pyenv install --skip-existing $(python_version) &&\
		pyenv uninstall -f $(python_env) &&\
		pyenv virtualenv --force $(python_version) $(python_env) &&\
		pyenv local $(python_env) &&\
		pip install --upgrade pip &&\
		pip install -e .[dev,build]

install:   ## install/reinstall python requirements into virtual env
		pip install --upgrade pip &&\
		pip install -e .[dev,build]

# ---------------------------------------------------------------------------- #
# test
# ---------------------------------------------------------------------------- #

pytest:  ## run pytest
	pytest $$(find ./tests -name '*.py')

black:  ## test code formatting with black
	black --config .flake8 $$(find ./src -name '*.py') --check

isort:  ## test import formatting with isort
	isort --profile="black" $$(find ./src -name '*.py') --check-only

mypy:   ## check types with mypy
	mypy --ignore-missing-imports --show-error-codes $$(find ./src -name '*.py')

test: black isort mypy pytest  ## run all tests

# ---------------------------------------------------------------------------- #
# document
# ---------------------------------------------------------------------------- #

build-docs:  ## build the documentation via sphinx
	cd $$PROJECT_DIR/docs &&\
		sphinx-apidoc -f -E -o source/ ../src/dsc &&\
		make html &&\
		cd -

clean-docs:  ## remove the documentation
	cd $$PROJECT_DIR/docs &&\
		make clean &&\
		cd -

rebuild-docs: clean-docs build-docs  ## rebuild (i.e. clean and build) all documentation via sphinx

# ---------------------------------------------------------------------------- #
# release
# ---------------------------------------------------------------------------- #

clean-dist:  ## clean the old distribution build
	if [ -d dist ]; then rm -rf dist; fi
	if [ -d $(package_name).egg-info ]; then rm -rf $(package_name).egg-info; fi

build-dist: clean-dist   ## distribution build
	python -m build

deploy-check:  ## pypi deployment check
	twine check dist/*

deploy-test-pypi: build-dist build-docs deploy-check  ## deployment to testpypi
	twine upload --verbose --skip-existing --repository testpypi dist/*

deploy-pypi: build-dist build-docs deploy-check  ## deployment to pypi
	twine upload --verbose dist/*