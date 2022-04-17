# spiget-orm

[![Build Status](https://github.com/PerchunPak/spiget-orm/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/spiget-orm/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/PerchunPak/spiget-orm/branch/master/graph/badge.svg)](https://codecov.io/gh/PerchunPak/spiget-orm)
[![Documentation Build Status](https://readthedocs.org/projects/spiget-orm/badge/?version=latest)](https://spiget-orm.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/spiget-orm)](https://www.python.org/downloads/)

ORM Spiget Python API Integration!

## Features

- Full support of ORM implementation!
- API version 2.


## Installing

```bash
pip install spiget-orm
```

## Installing for local developing

```bash
git clone https://https://github.com/PerchunPak/spiget-orm.git
cd spiget-orm
```

Then install `poetry` [recommended way](https://python-poetry.org/docs/master/#installation).

If you are on a Linux, use:

```bash
curl -sSL https://install.python-poetry.org | python -
```

If you are on a Windows, open PowerShell with admin name and use:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

And finally install all dependencies:

```bash
poetry install -E docs
```

## Example

```py
>>> from spiget_orm import some_function
>>> some_function(3, 4)
Currently in work!
```

## Thanks

This project was generated with [`fire-square-style`](https://github.com/fire-square/fire-square-style). 
Current template version is: [ff1d39cd7761f748d90b9c07bc280b5ee03dc5ba](https://github.com/fire-square/fire-square-style/tree/ff1d39cd7761f748d90b9c07bc280b5ee03dc5ba). 
See what is [updated](https://github.com/fire-square/fire-square-style/compare/ff1d39cd7761f748d90b9c07bc280b5ee03dc5ba...master) 
since then.
