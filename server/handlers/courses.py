from flask import Blueprint, jsonify, request, make_response, current_app
from middleware.auth import token_required
from typing import List, Dict
from models import Customer, Course
from workflows import acceses
import repository


courses_handler = Blueprint('courses_handler', __name__)


@courses_handler.route('/', methods=['GET'])
@token_required
def getCourses(customer: Customer):
    """
        get all bought courses for a customer
    """
    if customer is None:
        print("No customer provided, this should not happen")
        return make_response(jsonify({'message': 'Invalid token'}), 406)
    
    courses = repository.courses.getCustomerCourses(customer.email)
    
    if len(courses) < repository.courses.count():
        customer_accesses = acceses.getCustomerAccess(customer.email, current_app.config['COURSES_SPECIAL_ACCESSES'])
        current_accesses = repository.customers.getCustomerAccesses(customer)
        for access in customer_accesses:
            print(f"{customer_accesses=}\n{current_accesses=}\n{access=}")
            if access in current_accesses:
                continue
            
            repository.courses.purchase(customer.id, access)
            
        if len(customer_accesses) != len(current_accesses):
            courses = repository.courses.getCustomerCourses(customer.email)
        
    return make_response(jsonify(courses), 200)

@courses_handler.route('/course', methods=['GET'])
@token_required
def getCourseDetails(customer: Customer, *args, **kwargs):
    """
        get course details
    """
    course_id = request.args.get('id')
    if customer is None or course_id is None:
        return make_response(jsonify({'message': 'unacceptable'}), 406)
    
    course: Course = repository.courses.getById(course_id)
    
    course_data:Dict = course.toJson()
    course_data['classes'] = course.Classes
    del course_data['course_data']
    
    return make_response(jsonify(course_data), 200)
