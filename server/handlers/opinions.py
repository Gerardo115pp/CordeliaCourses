from flask import Blueprint, jsonify, request, make_response, current_app
from typing import List, Dict
from models import Opinion, Course, Customer
from middleware.auth import token_required
import Http.opinions as requests_forms
from Http.opinions import PostNewOpinionRequest as opinion_form
import repository
from dataclasses import asdict

opinions_handler = Blueprint('opinions_handler', __name__)

@opinions_handler.route('/opinion', methods=['POST'])
@token_required
def postOpinion(current_customer: Customer):
    """ 
        post a new opinion
    """
    request_data: opinion_form = requests_forms.createRequest(opinion_form, request.json)
    if not request_data:
        return make_response(jsonify({'message': 'missing fields'}), 406)
    
    if not repository.courses.getById(request_data.course_id):
        return make_response(jsonify({'message': 'class not found'}), 404)
    
    opinion = Opinion(course_id=request_data.course_id,
                        class_id=request_data.class_id,
                        customer_id=current_customer.id,
                        body=request_data.body,
                        username=f"{current_customer.name} {current_customer.last_name}",
                        isodate=request_data.isodate
                      )

    repository.opinions.insert(opinion)
    
    return make_response("", 201)

@opinions_handler.route('/opinion', methods=['GET'])
def getClassOpinions():
    """ 
        get all opinions by class and course
    """
    class_id = request.args.get('class_id')
    course_id = request.args.get('course_id')
    if not class_id or not course_id:
        return make_response(jsonify({'message': 'missing fields'}), 406)
    course_id = int(course_id)
    
    opinions = repository.opinions.getByClassCourse(class_id, course_id)
    serialized_opinions = [asdict(opinion) for opinion in opinions]
    return make_response(jsonify(serialized_opinions), 200)