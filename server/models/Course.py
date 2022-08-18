from dataclasses import dataclass
from datetime import datetime
from os.path import exists
from typing import List


def allArgsPresent(obj: object, args: List[str]) -> bool:
    """ 
        this method should be reassigned from the __init__.py file
    """
    raise NotImplementedError("this shouldnt happen")


""" 
DB structure:

+--------------+------------------+------+-----+---------+----------------+
| Field        | Type             | Null | Key | Default | Extra          |
+--------------+------------------+------+-----+---------+----------------+
| id           | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name         | varchar(100)     | NO   |     | NULL    |                |
| description  | varchar(255)     | NO   |     | NULL    |                |
| teacher_name | varchar(120)     | NO   |     | NULL    |                |
| course_data  | varchar(255)     | NO   |     | NULL    |                |
+--------------+------------------+------+-----+---------+----------------+
"""


@dataclass
class Course:
    name: str
    description: str
    teacher_name: str
    course_data: str
    id: int = None
    
    @staticmethod
    def create(name: str, description: str, teacher_name: str, course_data: str, id:int=None) -> 'Course':
        """ 
            creates a new course object, it expects all the fields to be present, if creating a new course, use Course.create() instead
        """
        raise NotImplementedError("create is not supported for Courses, they should be created manually")
    
    @staticmethod
    def recreate(**kwargs) -> 'Course':
        """ 
            creates a new course object from the given kwargs, it expects all the fields to be present, if creating a new course, use Course.create() instead
        """
        assert allArgsPresent(Course, kwargs), f"{kwargs} are not all present in Course.create"
        
        if not exists(kwargs['course_data']):
            print(f"WARNING: course_data {kwargs['course_data']} does not exist <course id={kwargs['id']}>")
        
        recreated_course = Course(**kwargs)
        return recreated_course
        

    