.PHONY: clean build test pypi

clean: 
	rm -rf build
	rm -rf dist
	rm -rf paper2img.egg-info

build:
	python setup.py install

test:
	python -m unittest -v paper2img/tests/*.py

pypi:
	python setup.py register
	python setup.py sdist bdist bdist_egg upload
