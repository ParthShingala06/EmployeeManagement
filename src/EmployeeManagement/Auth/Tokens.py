from uuid import uuid4
from flask import request

from EmployeeManagement.Models.Token import Token

tokens = {}

def newUser():
    token = str(uuid4())
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    tokens[token] = Token(name, email)
    print(tokens)
    return {'Your Access Token': token }

def verifyToken():
    # Access a specific header
    token = request.headers.get('X-Api-Key')
    if token in tokens.keys():
        print("Found")
        return token
    return None