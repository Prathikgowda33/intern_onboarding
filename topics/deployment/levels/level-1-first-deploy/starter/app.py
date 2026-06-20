"""
Flask app for Deployment Level 1 — First Deploy.

This app reads an environment variable and displays it.
Deploy to Railway.app without modifications.

Do NOT modify this file unless a constraint requires it.
"""

import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read the environment variable, with a default fallback
APP_ENVIRONMENT = os.environ.get("APP_ENVIRONMENT", "development")


@app.route("/")
def index():
    return f"Hello from {APP_ENVIRONMENT}! Environment: {APP_ENVIRONMENT}\n"


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "environment": APP_ENVIRONMENT,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
