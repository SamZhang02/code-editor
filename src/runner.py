import uuid
import os
import time
from datetime import datetime
import subprocess

from src.models import CodeResult


def run_code_in_docker(code: str) -> CodeResult:

    code_filename = f"user_code_{uuid.uuid4().hex}.py"
    code_filepath = os.path.join("/tmp", code_filename)

    with open(code_filepath, "w") as f:
        f.write(code)

    start_time = time.time()
    timestamp = datetime.now().isoformat()

    try:
        result = subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "-v",
                f"/tmp:/app:ro",
                "--network",
                "none",
                "--cpus",
                "1",
                "--memory",
                "512m",
                "python-numpy-pandas",
                "python",
                f"/app/{code_filename}",
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )
        output = result.stdout
        error = result.stderr
        execution_time = time.time() - start_time
        status = "error" if error else "success"
    except subprocess.TimeoutExpired:
        status = "error"
        output = None
        error = "Timeout: Code ran for longer than 10 seconds."
        execution_time = None
    finally:
        os.remove(code_filepath)

    return CodeResult(
        status=status,
        timestamp=timestamp,
        stdout=output,
        stderr=error,
        time_ran=execution_time,
    )
