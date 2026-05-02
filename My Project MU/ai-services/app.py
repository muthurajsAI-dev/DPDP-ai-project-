import sys
import os
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from services.sanitizer import sanitize_input

app = Flask(__name__)

# Initialize the rate limiter (AI Developer 3 Task)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"],
    storage_uri="memory://",
)

@app.route('/describe', methods=['POST'])
@limiter.limit("10 per minute")  # Extra security for the AI route
def describe():
    data = request.json
    user_text = data.get("text", "")

    cleaned_text, is_safe = sanitize_input(user_text)

    if not is_safe:
        return jsonify({
            "status": "error",
            "message": "Unsafe input detected!"
        }), 400

    return jsonify({
        "status": "success",
        "cleaned_text": cleaned_text,
        "message": "Input is safe and sanitized"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)