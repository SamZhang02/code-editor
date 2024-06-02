FROM python:3.11

RUN pip install numpy pandas scipy

WORKDIR /app

CMD ["python", "/app/user_code.py"]
