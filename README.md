# exopypi

[PEP691](https://peps.python.org/pep-0691/) compliant python package repository with mirroring
and pluggable storage backends.

Made to be used in remote (exo) locations with limited internet access.

## Development

This project uses [rye](https://rye.astral.sh/guide/) to manage the python environment, dependencies and run configurations.
To install [rye](https://rye.astral.sh/guide/) follow the
[installation instructions](https://rye.astral.sh/guide/installation) for your platform.

```shell
rye sync --no-lock
rye run pre-commit install --install-hooks
rye run dev
```
