from pydantic import BaseModel
from typing import Literal, Optional


class CodeResult(BaseModel):
    status: Literal["success"] | Literal["error"]
    stdout: Optional[str]
    stderr: Optional[str]
    time_ran: Optional[float]
    timestamp: str