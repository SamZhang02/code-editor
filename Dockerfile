FROM python:3.11

RUN pip install numpy pandas

WORKDIR /app

CMD ["python", "/app/user_code.py"]
