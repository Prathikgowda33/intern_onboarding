from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

bookmarks = []
next_id = 1

def find_bookmark(bookmark_id):
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            return bookmark
    return None

@app.route("/bookmarks", methods=["GET"])
def get_bookmarks():
    return jsonify(bookmarks), 200

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

    if "title" in data:
        bookmark["title"] = data["title"]

    if "url" in data:
        bookmark["url"] = data["url"]

    if "tags" in data:
        bookmark["tags"] = data["tags"]

    return jsonify(bookmark), 200

@app.route("/bookmarks/<int:bookmark_id>", methods=["DELETE"])
def delete_bookmark(bookmark_id):
    bookmark = find_bookmark(bookmark_id)

    if bookmark is None:
        return jsonify({"error": "Bookmark not found"}), 404

    bookmarks.remove(bookmark)

    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
