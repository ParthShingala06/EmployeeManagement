from uuid import uuid4
from flask import request

from EmployeeManagement.Models.Token import Token

tokens = {}

def newUser():
    token = str(uuid4())
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    role = "Admin" if email == "parth.shingalaa@gmail.com" else "User"
    tokens[token] = Token(name, email, role)
    return {'Your Access Token': token }

def verifyToken():
    # Access a specific header
    token = request.headers.get('X-Api-Key')
    if token in tokens.keys():
        return token
    return None