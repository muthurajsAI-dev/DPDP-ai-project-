import jwt
from flask import request, jsonify
from functools import wraps

# ADD IT HERE - This must match the key in app.py exactly!
SECRET_KEY = 'Muthuraj_DPDP_AI_Project_Secure_2026_Key_Long'
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Check if the token is in the headers
        if 'Authorization' in request.headers:
            # Look for "Bearer <token>"
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # Use the SECRET_KEY to unlock and read the token
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user']
        except Exception as e:
            return jsonify({'message': 'Token is invalid or expired!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated