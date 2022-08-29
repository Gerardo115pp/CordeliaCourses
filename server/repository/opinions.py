from typing import List, Dict, Any
from models import Opinion

class OpinionRepoMeta(type):
    """ 
        A metaclass for customers repository
    """
    
    def __instancecheck__(cls, __instance: Any) -> bool:
        return cls.__subclasscheck__(type(__instance))
    
    def __subclasscheck__(cls, subclass: Any) -> bool:
        return (hasattr(subclass, 'getByClassCourse') and  callable(subclass.getByClassCourse)) and \
                (hasattr(subclass, 'insert') and  callable(subclass.insert))
                

class OpinionRepo(metaclass=OpinionRepoMeta):
    """
        A interface for customers repository
    """
    
    def getByClassCourse(self, class_id: str, course_id: int) -> List[Opinion]:
        """
            Returns all opinions by class and course
        """
        raise NotImplementedError()
    
    def insert(self, opinion: Opinion) -> None:
        """
            Inserts a opinion
        """
        raise NotImplementedError()
    
implementation: OpinionRepo = None

def setRepository(repo: OpinionRepo) -> None:
    """
        Sets the customers repository
    """
    global implementation
    assert isinstance(repo, OpinionRepo), "repo must be an instance of OpinionRepo"
    implementation = repo
    
def getByClassCourse(class_id: str, course_id: int) -> List[Opinion]:
    """
        Returns all opinions by class and course
    """
    return implementation.getByClassCourse(class_id, course_id)

def insert(opinion: Opinion) -> None:
    """
        Inserts a opinion
    """
    return implementation.insert(opinion)