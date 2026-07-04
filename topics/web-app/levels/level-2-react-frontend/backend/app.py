from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["http://localhost:5173"])

entries = []


@app.route("/api/entries", methods=["GET"])
def get_entries():
    return jsonify(entries), 200


@app.route("/api/entries", methods=["POST"])
def add_entry():
    data = request.get_json()

    name = data.get("name", "").strip()
    message = data.get("message", "").strip()

    entry = {
        "name": name,
        "message": message
    }

    entries.append(entry)

    return jsonify(entry), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
