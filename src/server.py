from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/health")
def health_check():
    return {"Hello": "World"}


class Result(BaseModel):
    status: Literal["success"] | Literal["error"]
    stdout: str
    stderr: str
    time_ran: str
    timestamp: str


@app.post("/code/test")
def test_code(code: str) -> Result:
    return Result(status="success", stdout="", stderr="", time_ran="0", timestamp="")


@app.post("/code/submit")
def submit_code(user_id: str, code: str) -> Result:
    return Result(status="success", stdout="", stderr="", time_ran="0", timestamp="")
