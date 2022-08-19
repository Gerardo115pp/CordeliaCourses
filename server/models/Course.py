from dataclasses import dataclass, asdict
from typing import List, Dict
from datetime import datetime
from os.path import exists
import json


CLASSES_FILE_NAME = "classes.json"
OPINIONS_FILE_NAME = "opinions.json"
SPECIAL_ACCESS_FILE_NAME = "special_access.json"

def allArgsPresent(obj: object, args: List[str]) -> bool:
    """ 
        this method should be reassigned from the __init__.py file
    """
    raise NotImplementedError("this shouldnt happen")

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
        
    @property
    def Classes(self) -> List[Dict]:
        with open(f"{self.course_data}/{CLASSES_FILE_NAME}", "r") as f:
            return json.load(f)

    def toJson(self) -> Dict:
        return asdict(self)