from flask import Flask, jsonify, request
from datetime import datetime
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

bookmarks = []
next_id = 1


def validate_bookmark(data):
    if not data:
        return "Request body must be JSON"

    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return "title is required and must be a non-empty string"

    url = data.get("url")
    if not isinstance(url, str) or not (
        url.startswith("http://") or url.startswith("https://")
    ):
        return "url is required and must start with http:// or https://"

    tags = data.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            return "tags must be a list of strings"

        for tag in tags:
            if not isinstance(tag, str):
                return "tags must be a list of strings"

    return None


def find_bookmark(bookmark_id):
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            return bookmark
    return None


@app.after_request
def log_request(response):
    app.logger.info(
        "%s %s %s",
        request.method,
        request.path,
        response.status_code
    )

    if response.status_code >= 500:
        app.logger.error("Server error")

    return response
@app.route("/bookmarks", methods=["GET"])
def get_bookmarks():
    tag = request.args.get("tag")

    if tag:
        filtered = [
            bookmark for bookmark in bookmarks
            if tag.lower() in [t.lower() for t in bookmark.get("tags", [])]
        ]
        return jsonify(filtered), 200

    return jsonify(bookmarks), 200


@app.route("/bookmarks/search", methods=["GET"])
def search_bookmarks():
    query = request.args.get("q", "").lower()

    results = [
        bookmark for bookmark in bookmarks
        if query in bookmark["title"].lower()
    ]

    return jsonify(results), 200


@app.route("/bookmarks/<int:bookmark_id>", methods=["GET"])
def get_bookmark(bookmark_id):
    bookmark = find_bookmark(bookmark_id)

    if bookmark is None:
        return jsonify({"error": "Bookmark not found"}), 404

    return jsonify(bookmark), 200


@app.route("/bookmarks", methods=["POST"])
def create_bookmark():
    global next_id

    data = request.get_json()

    error = validate_bookmark(data)
    if error:
        app.logger.warning(error)
        return jsonify({"error": error}), 400

    bookmark = {
        "id": next_id,
        "title": data["title"],
        "url": data["url"],
        "tags": data.get("tags", []),
        "created_at": datetime.now().isoformat()
    }

    bookmarks.append(bookmark)
    next_id += 1

    return jsonify(bookmark), 201
@app.route("/bookmarks/<int:bookmark_id>", methods=["PUT"])
def update_bookmark(bookmark_id):
    bookmark = find_bookmark(bookmark_id)

    if bookmark is None:
        return jsonify({"error": "Bookmark not found"}), 404

    data = request.get_json()

    error = validate_bookmark(data)
    if error:
        app.logger.warning(error)
        return jsonify({"error": error}), 400

    bookmark["title"] = data["title"]
    bookmark["url"] = data["url"]
    bookmark["tags"] = data.get("tags", [])

    return jsonify(bookmark), 200


@app.route("/bookmarks/<int:bookmark_id>", methods=["DELETE"])
def delete_bookmark(bookmark_id):
    bookmark = find_bookmark(bookmark_id)

    if bookmark is None:
        return jsonify({"error": "Bookmark not found"}), 404

    bookmarks.remove(bookmark)
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

