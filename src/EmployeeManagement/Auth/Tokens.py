from functools import wraps
from uuid import uuid4
from flask import jsonify, request

from EmployeeManagement.Models.Token import Token

tokens = {}

def newUser():
    token = str(uuid4())
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    role = "Admin" if email.lower() == "parth.shingalaa@gmail.com" else "User"
    tokens[token] = Token(name, email, role)
    return {'Your Access Token': token }

def verifyToken():
    # Access a specific header
    token = request.headers.get('X-Api-Key')
    if token in tokens.keys():
        return token
    return None

def role_auth(required_role, auth):
    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            token = auth.current_user()  # Get the current authenticated token
            user = tokens.get(token)
            if not user:
                return jsonify({"message": "Unauthorized"}), 401
            if user.Role != required_role:
                return jsonify({"message": "Forbidden: Insufficient permissions"}), 403
            return func(*args, **kwargs)
        return decorated_function
    return wrapper