SHELL := /bin/bash #to be able to execute `source`

.PHONY: build clean test upload docs
build: clean
	python setup.py sdist bdist_wheel
	
clean:
	rm -rf dist */*.egg-info *.egg-info  build
	rm -rf .test

testupload: build
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose

test: build
	virtualenv .test
	source .test/bin/activate
	pip install dist/*.whl
	pytest

upload: build
	twine check dist/*
	twine upload dist/* --verbose