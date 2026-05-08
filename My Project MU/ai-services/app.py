import jwt
from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta, timezone
from routes.ai_routes import ai_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Muthuraj_DPDP_AI_Project_Secure_2026_Key_Long'

# This makes the AI route accessible at /ai/chat
app.register_blueprint(ai_bp, url_prefix='/ai')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get('username') == 'admin' and data.get('password') == 'password123':
        token = jwt.encode({
            'user': 'admin',
            'exp': datetime.now(timezone.utc) + timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({"status": "success", "access_token": token})
    return jsonify({"status": "error", "message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)