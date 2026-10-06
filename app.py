import os
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)
STARTED_AT = datetime.now(timezone.utc).isoformat()
# Anything you add under "Variables" in ZeroTo shows up here. Try adding GREETING and redeploying.
GREETING = os.environ.get("GREETING", "Hello from my first Flask app")


@app.get("/")
def index():
    return jsonify(message=GREETING, started_at=STARTED_AT)


@app.get("/health")
def health():
    return jsonify(ok=True)


if __name__ == "__main__":
    # Only for running on your laptop (python app.py). On ZeroTo, gunicorn starts the app (see Procfile).
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
