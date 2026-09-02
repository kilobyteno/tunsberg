# Tunsberg
[![codecov](https://codecov.io/gh/kilobyteno/tunsberg/graph/badge.svg?token=4f1MOyWq6b)](https://codecov.io/gh/kilobyteno/tunsberg)
[![PyPI version](https://badge.fury.io/py/tunsberg.svg)](https://badge.fury.io/py/tunsberg)
[![Downloads](https://pepy.tech/badge/tunsberg)](https://pepy.tech/project/tunsberg)
[![License](https://img.shields.io/github/license/kilobyteno/tunsberg)](LICENSE.md)

A collection of opinionated methods, functions, classes and utils for Python, FastAPI and related libraries.

Supports Python 3.11 and newer. Local development defaults to Python 3.12 via [`.python-version`](.python-version).

## Installation

```bash
pip install tunsberg
```

## Development

This project uses [uv](https://docs.astral.sh/uv/). After cloning:

```bash
uv sync --group dev
uv run pre-commit install
```

When you change dependencies in `pyproject.toml`, refresh the lockfile and commit it:

```bash
uv lock
```

## Usage

See the [docs index](docs/README.md) for `responses`, `konfig`, and `utsikten`.

## Testing

```bash
uv run pytest
```

Lint and format:

```bash
uv run ruff check
uv run ruff format
```

## Releasing

1. Bump `__version__` in `tunsberg/__init__.py` on `main`.
2. Create a GitHub release whose tag matches that version (for example `0.4.0`, or `v0.4.0`).
3. The release workflow validates the tag against `__version__`, builds, and publishes to PyPI.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
