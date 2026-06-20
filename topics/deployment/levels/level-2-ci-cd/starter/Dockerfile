# Dockerfile for Deployment Level 2 — CI/CD
# TODO: Complete the ARG and ENV lines to pass COMMIT_HASH through

FROM python:3.11-slim

# TODO: Add an ARG for COMMIT_HASH so it can be passed at build time
# ARG COMMIT_HASH

# TODO: Set COMMIT_HASH as an environment variable so the app can read it at runtime
# ENV COMMIT_HASH=${COMMIT_HASH}

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
