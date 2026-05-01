from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize limiter
limiter = Limiter(
    get_remote_address,  # tracks user by IP
    app=app,
    default_limits=["30 per minute"]  # global limit
)

# Sample API
@app.route('/describe', methods=['POST'])
@limiter.limit("10 per minute")  # stricter limit
def describe():
    return jsonify({
        "message": "Request successful"
    })

# Health check
@app.route('/health')
def health():
    return {"status": "running"}

if __name__ == '_main_':
    app.run(port=5000, debug=True)