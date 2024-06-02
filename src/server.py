from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from src.models import CodeResult
from src.runner import run_code_in_docker
from src.db import Database, DatabaseError

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
api_router = APIRouter(prefix="/api")

database = Database("code_editor.db")
database.initialize_tables()


@app.get("/health")
def health_check():
    return {"Hello": "World"}


class CodeRequest(BaseModel):
    code: str


@api_router.post("/code/test")
def test_code(request: CodeRequest) -> CodeResult:
    return run_code_in_docker(request.code)


@api_router.post("/code/submit")
def submit_code(request: CodeRequest) -> CodeResult:
    result = run_code_in_docker(request.code)

    if result.status == "success":
        try:
            database.add_submission(result.timestamp, request.code)
        except DatabaseError as e:
            result.status = "error"
            result.stderr = str(e)

    return result

app.include_router(api_router)
