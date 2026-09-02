# Contributing
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a contributor

## We Develop with GitHub
We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. Install dependencies with [uv](https://docs.astral.sh/uv/): `uv sync --group dev`.
3. Install git hooks: `uv run pre-commit install`.
4. If you change dependencies in `pyproject.toml`, run `uv lock` and commit `uv.lock`.
5. If you've added code that should be tested, test it with `uv run pytest`.
6. Run `uv run ruff check` and `uv run ruff format` before opening a pull request.
7. Ensure your commits have descriptive text.
8. Issue that pull request!

Please also follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Any contributions you make will be under the License
In short, when you submit code changes, your submissions are understood to be under the same [license](../LICENSE.md) that
covers the project.

## Reporting bugs
We use GitHub [issues](https://github.com/kilobyteno/tunsberg/issues) to track public bugs. Report a bug by opening a new issue; it's that easy! Write bug
reports with detail, this makes it a lot easier to understand the issue.

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce. Be specific!
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)
