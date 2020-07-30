
.PHONY: all

all: clean test

clean:
	find . | grep -E "\(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf

test:
	PYTHONPATH=. py.test -vv --cov=opendssdirect tests
	export DSS_EXTENSIONS_DEBUG=1
	PYTHONPATH=. py.test -vv tests

html:
	@cd docs; pandoc ../README.md -o readme.rst; make html

github: html
	-git branch -D gh-pages
	-git push origin --delete gh-pages
	ghp-import -n -b gh-pages -m "Update documentation" docs/_build/html
	git checkout gh-pages
	git push --set-upstream origin gh-pages
	git checkout master

