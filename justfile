set dotenv-load

default:
  just --list

fmt: 
  pnpm run format

serve:
  poetry run src/server.py

ui:
  npm run dev

dev:
  serve && npm run dev



