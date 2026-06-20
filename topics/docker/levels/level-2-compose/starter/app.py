"""
Flask app skeleton with Redis integration TODOs.

Complete this app to use Redis for storing the visit counter.
Connect to Redis at hostname 'redis' (the compose service name), port 6379.

NOTE: Complete the TODO sections. The overall structure is provided.
"""

from flask import Flask, jsonify
import redis  # TODO: install this (pip install redis)

app = Flask(__name__)

# TODO: Connect to Redis at hostname 'redis', port 6379, db 0
# Example: r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
r = None  # TODO: replace with actual Redis connection


@app.route("/")
def index():
    # TODO: Use Redis INCR to increment a counter key (e.g., "visit_count")
    # TODO: Return f"Hello! You are visitor #{count}"
    return "Hello! TODO: implement Redis counter\n"


@app.route("/health")
def health():
    # TODO: Ping Redis to check connection
    # TODO: Return JSON with status and redis connection state:
    #   {"status": "ok", "redis": "connected"} or {"status": "ok", "redis": "disconnected"}
    return jsonify({"status": "ok", "redis": "todo"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
