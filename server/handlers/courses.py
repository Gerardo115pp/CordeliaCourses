from flask import Blueprint, jsonify, request, make_response, current_app
from middleware.auth import token_required
from typing import List, Dict
from models import Customer, Course
import repository


courses_handler = Blueprint('courses_handler', __name__)


@courses_handler.route('/course', methods=['GET'])
@token_required
def getCourses(customer: Customer):
    """
        get all courses
    """
    courses = repository.courses.getCustomerCourses(customer.email)
    return make_response(jsonify(courses), 200)