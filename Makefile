
.PHONY: all

all: clean test

clean:
	find . | grep -E "\(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf

test:
	@cd tests; PYTHONPATH=.. py.test --tb=short


