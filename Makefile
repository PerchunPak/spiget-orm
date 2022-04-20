SHELL:=/usr/bin/env bash

.PHONY: lint
lint: style

.PHONY: style
style:
	poetry run black .
	poetry run isort .
	poetry run pycln .
	poetry run mypy --install-types --non-interactive spiget_orm tests
	poetry run flake8 .
	poetry run doc8 -q docs

.PHONY: unit
unit:
# This will run pycln if not in CI
ifeq ($(CI),)
	poetry run pytest
else
	poetry run pytest --no-testmon
endif

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit
