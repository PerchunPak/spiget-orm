# How to contribute


## Dependencies

We use [poetry](https://github.com/python-poetry/poetry) to manage the dependencies.

To install them you would need to run `install` command:

```bash
poetry install
```

Also lets install `pre commit hooks` in `git`:
```bash
poetry run pre-commit install
```

To activate your `virtualenv` run `poetry shell`.


## One magic command

Run `make test` to run everything we have!


## Tests

We use  `black`, `flake8` и `pytest` for quality control.

To run formatter:

```bash
black .
```

To run linter (it checks only docstrings, [more info](http://www.pydocstyle.org/en/latest/error_codes.html)):
```bash
flake8 .
```

To run all tests:

```bash
pytest
```

If you want to configure some utils, you need do it in `setup.cfg`.
These steps are mandatory during the CI.


## Type checks

We use `mypy` to run type checks on our code.
To use it:

```bash
mypy mc_plugin_helper tests
```

This step is mandatory during the CI.

## Before submitting

Before submitting your code please do the following steps:

1. Run `pytest` to make sure everything was working before
2. Add any changes you want
3. Add tests for the new changes
4. Edit documentation if you have changed something significant
5. Update `CHANGELOG.md` with a quick summary of your changes
6. Run `pytest` again to make sure it is still working
7. Run `mypy` to ensure that types are correct
8. Run `black` to ensure that style is correct
9. Run `doc8` and `flake8` to ensure that docs are correct


## Other help

You can contribute by spreading a word about this tool.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
