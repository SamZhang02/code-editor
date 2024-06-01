from fastapi import FastAPI
from models import CodeResult
from src.runner import run_code_in_docker

from db import Database

app = FastAPI()
database = Database("code_editor.db")
database.initialize_tables()

@app.get("/health")
def health_check():
    return {"Hello": "World"}


@app.post("/code/test")
def test_code(code: str) -> CodeResult:
    return run_code_in_docker(code)


@app.post("/code/submit")
def submit_code(code: str) -> CodeResult:
    result = run_code_in_docker(code)

    if result.status == "success":
        database.add_submission(result.timestamp, code)

    return result
