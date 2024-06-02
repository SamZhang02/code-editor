# Simple online Python 3.11 Code Editor

This is a take home assignment for a job position at a cool company.

https://github.com/SamZhang02/code-editor/assets/112342947/b597a5f4-fbf1-4624-ae12-21085b682f22

The website is an online code editor for Python 3.11, with a `test code` button
thats runs the code, and a `submit` button to persist the code into a database.

## Prerequisites

- Python3
- Poetry
- npm
- Docker
- just (optional)

You should first build a Docker container with the image containing Python 3.11,
numpy, pandas and scipy with one of the following commands.

The backend Python's package management is done using `Poetry`, and the
frontend's package management is done using `npm`.

You can find an
[overview](https://github.com/SamZhang02/code-editor/blob/main/docs/OVERVIEW.md)
of the codebase's key elements in `/docs`.

```shell
just build-container
```

```shell
docker build -t python-numpy-pandas .
```

This is the container image for where user submitted codes will be ran.

## Running the project

I use `just` as a script runner, with available scripts located in the
`justfile`, for functionalities such as formatting, testing, etc.

From the root directory of the project, to launch the frontend, use one of the
following commands below

```shell
just ui
```

```shell
npm run dev
```

And one of the following commands for the backend:

```shell
just serve
```

```shell
poetry run fastapi dev src/server.py
```

## Running tests

There are a couple simple test cases for the backend of the project, testing for
correct functioning of some components, including their security against
malicious user submissions. To run tests, use one of the following commands

```shell
just test
```

```shell
poetry run pytest src/tests
```
