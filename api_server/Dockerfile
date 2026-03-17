FROM python:3.11-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8085

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8085"]