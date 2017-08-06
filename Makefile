
.PHONY: all

all: clean test

clean:
	find . | grep -E "\(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf

test:
	PYTHONPATH=. py.test -vv --cov=opendssdirect tests

html:
	@cd docs; pandoc ../README.md -o readme.rst; make html

github: html
	-git branch -D gh-pages
	-git push origin --delete gh-pages
	ghp-import -n -b gh-pages -m "Update documentation" docs/_build/html
	git checkout gh-pages
	git push
	git checkout master

