FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app.py .

RUN useradd --create-home appuser && chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
