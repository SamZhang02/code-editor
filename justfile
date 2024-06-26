set dotenv-load

default:
  just --list

fmt: 
  poetry run black src
  npm run format

serve:
  poetry run fastapi dev src/server.py

ui:
  npm run dev

test *args:
  poetry run pytest src/tests {{args}}

build-container:
  docker build -t python-numpy-pandas .

