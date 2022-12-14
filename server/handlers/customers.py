from flask import Blueprint, jsonify, request, make_response, current_app
from typing import List, Dict
from models import Customer
from middleware.auth import getTokenString
from workflows.acceses import createCustomerAccesses
import Http.customers as requests_forms
from Http.customers import LoginPasswordCustomerRequest as login_form, CreatePasswordCustomerRequest as register_form
import repository
import json
import jwt
from datetime import datetime, timedelta
import os

customers_handler = Blueprint('customers_handler', __name__)



@customers_handler.route('/customer', methods=['POST'])
def createCustomer():
    """ 
        register a new customer with password only
    """
    
    if not all(key in request.json for key in ['name', 'last_name', 'email', 'password']):
        return make_response(jsonify({'message': 'missing fields'}), 406)
    print("Customer fields are valid")
    
    if repository.customers.getByEmail(request.json['email']):
        print("Customer already exists")
        return make_response(jsonify({'message': 'email already registered'}), 409)
    print(f"Registering new customer {request.json['email']}")
    
    
    customer = Customer.create(request.json["name"], request.json["last_name"], request.json["email"], password=request.json["password"])
    repository.customers.insert(customer)
    print(f"Customer {customer.email} registered on repository")
    
    special_access_map = current_app.config['COURSES_SPECIAL_ACCESSES']
    createCustomerAccesses(customer, special_access_map) # looks for the accesses the customer has purchased and creates them in the repository
    print(f"Customer {customer.email} accesses created")
    
    
    print(f"created customer {customer.id} with email {customer.email}")
    return make_response("", 201)


@customers_handler.route('/customer/auth', methods=['POST'])
def authenticateCustomer():
    request_data: login_form = requests_forms.createRequest(login_form, request.json)
    target_customer = repository.customers.getByEmail(request_data.email)
    if not target_customer:
        return jsonify({'message': 'email not registered'}), 404
    
    correct_password = target_customer.auth(request_data.password)
    if not correct_password:
        return make_response(jsonify({'message': 'invalid password'}), 401)
    
    # tokens expire in 30 days
    jwt_secret = current_app.config['JWT_SECRET']
    expiration_time = timedelta(days=30)
    jwt_payload = {
        'id': target_customer.id,
        'email': target_customer.email,
        'name': target_customer.name,
        'last_name': target_customer.last_name,
        'exp': datetime.utcnow() + expiration_time
    }
    
    # TODO: add expiration to the token
    
    jwt_token = jwt.encode(jwt_payload, jwt_secret, algorithm='HS256')
    return make_response(jsonify({'token': jwt_token}), 200)

@customers_handler.route('customer/password', methods=['PATCH'])
def changePassword():
    token_string = getTokenString(request.headers)
    jwt_secret = current_app.config['JWT_SECRET']
    
    try:
        jwt_headers = jwt.get_unverified_header(token_string)
        data = jwt.decode(token_string, jwt_secret, algorithms=[jwt_headers['alg']])
        token_payload = {
            "email": data['email'],
            "customer": data['customer'],
            "exp": data['exp']
        }
    except jwt.InvalidSignatureError:
        print(f"Someone is doing something fishy with the token: {token_string}")
        return make_response(jsonify({'message': 'invalid token'}), 401)
    except jwt.ExpiredSignatureError:
        print(f"Expired token: {token_string}")
        return make_response(jsonify({'message': 'token expired'}), 408)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'invalid token'}), 401)
    
    new_password = request.json['password']
    if len(new_password) < 8:
        return make_response(jsonify({'message': 'password too short'}), 406)
    
    customer: Customer = repository.customers.getByEmail(token_payload['email'])
    customer.changePassword(new_password)
    
    repository.customers.updatePassword(customer)
    return make_response(jsonify({'message': 'password changed'}), 200)
    
    
    
    
    