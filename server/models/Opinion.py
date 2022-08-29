from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any

def allArgsPresent(obj: object, args: List[str]) -> bool:
    """ 
        this method should be reassigned from the __init__.py file
    """
    raise NotImplementedError("this shouldnt happen")

@dataclass
class Opinion:
    
    customer_id: str
    course_id: int
    class_id: str
    username: str
    body: str
    isodate: str
    id: int=None
    
    
    @staticmethod
    def create(course_id: str, customer_id: str, username: str, body: str, isodate: str) -> 'Opinion':
        """ 
            creates a new opinion object, it expects all the fields to be present, if creating a new opinion, use Opinion.create() instead
        """
        
        new_opinion = Opinion(customer_id=customer_id, username=username, body=body, isodate=isodate)
        return new_opinion

    @staticmethod
    def recreate(**kwargs) -> 'Opinion':
        """ 
            creates a new opinion object from the given kwargs, it expects all the fields to be present, if creating a new opinion, use Opinion.create() instead
        """
        assert allArgsPresent(Opinion, kwargs), f"{kwargs} are not all present in Opinion.create"
        
        new_opinion = Opinion(**kwargs)
        return new_opinion