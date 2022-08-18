from flask import  current_app ,request, jsonify
from datetime import datetime, timedelta
from functools import wraps
from typing import Callable
from inspect import getfullargspec
import models
import jwt
import os


def token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        jwt_secret = current_app.config.get('JWT_SECRET')
        assert jwt_secret is not None, 'JWT_SECRET must be set'
        
        token = request.headers.get('Authorization', "")
        token = token.removeprefix('Bearer ')
        
        if token == "":
            print("No token provided")
            return jsonify({"message": "Missing token"}), 401

        customer: models.Customer = None
        try:
            jwt_header = jwt.get_unverified_header(token)
            data = jwt.decode(token, jwt_secret, algorithms=[jwt_header['alg']])
            customer = models.Customer(id=data['id'], email=data['email'], name=data['name'], last_name=data['last_name'], last_item_check=datetime.now().timestamp())
        except Exception as e:
            print(f"Error decoding token: {e}")
            return jsonify({"message": "Invalid token"}), 401
        
        if len(getfullargspec(f).args) == 1:
            return f(customer, *args, **kwargs)
        else:
            return f(*args, **kwargs)

    return decorated