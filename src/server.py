from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import logging

from src.models import CodeResult
from src.runner import run_code_in_docker
from src.db import Database, DatabaseError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"], # For the take home assignment, I simply allowed all origins for CORS. In a production environment, this would be the frontend's url instead.
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
    logger.info("Received code, testing...")
    result = run_code_in_docker(request.code)
    logger.info(f"Code tested, status {result.status}")

    return result


@api_router.post("/code/submit")
def submit_code(request: CodeRequest) -> CodeResult:
    logger.info("Received code, testing...")
    result = run_code_in_docker(request.code)
    logger.info(f"Code tested, status {result.status}")

    if result.status == "success":
        try:
            logger.info("Writing code to db...")
            database.add_submission(result.timestamp, request.code)
            logger.info("Code has been written to db.")
        except DatabaseError as e:
            logger.info(f"Wring to db failed, error: {e}")
            result.status = "error"
            result.stderr = str(e)


    return result


app.include_router(api_router)
