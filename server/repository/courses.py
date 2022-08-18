from typing import List, Dict, Any
from models import Course

class CoursesRepoMeta(type):
    """
        A metaclass for courses repository
    """

    def __instancecheck__(cls, __instance: Any) -> bool:
        return cls.__subclasscheck__(type(__instance))

    def __subclasscheck__(cls, subclass: Any) -> bool:
        return (hasattr(subclass, 'count') and  callable(subclass.count)) and \
                (hasattr(subclass, 'getAll') and  callable(subclass.getAll)) and \
                (hasattr(subclass, 'getById') and  callable(subclass.getById)) and \
                (hasattr(subclass, 'getSpecialAccessMap') and  callable(subclass.getSpecialAccessMap)) and \
                (hasattr(subclass, 'getCustomerCourses') and  callable(subclass.getCustomerCourses)) and \
                (hasattr(subclass, 'purchase') and  callable(subclass.purchase))
                    
                    
                
class CoursesRepo(metaclass=CoursesRepoMeta):
    """
        A interface for courses repository
    """
    def count(self) -> int:
        """
            Returns the number of courses
        """
        raise NotImplementedError()

    def getAll(self) -> List[Course]:
        """
            Returns all courses
        """
        raise NotImplementedError()

    def getById(self, id: str) -> Course:
        """
            Returns a course by id
        """
        raise NotImplementedError()
    
    def getSpecialAccessMap() -> Dict[int, str]:
        """ 
            return a dict mapping course id to its course_data which is the directory where its data
            is stored
        """
        return NotImplementedError()
    
    def getCustomerCourses(self, email: str) -> List[Course]:
        """
            Returns all courses for a customer
        """
        raise NotImplementedError()
    
    def purchase(self, customer_id: str, access_id: int) -> bool:
        """
            purchase a course access for a customer
        """
        raise NotImplementedError()
    
implementation: CoursesRepo = None

def setRepository(repo: CoursesRepo) -> None:
    """
        Sets the courses repository
    """
    global implementation
    assert isinstance(repo, CoursesRepo), f"{repo} is not an instance of CoursesRepo"
    implementation = repo
    
def count() -> int:
    """
        Returns the number of courses
    """
    return implementation.count()
    
def getAll() -> List[Course]:
    """
        Returns all courses
    """
    return implementation.getAll()

def getById(id: str) -> Course:
    """
        Returns a course by id
    """
    return implementation.getById(id)

def getSpecialAccessMap() -> Dict[int, str]:
    """ 
        return a dict mapping course id to its course_data which is the directory where its data
        is stored
    """
    return implementation.getSpecialAccessMap()

def getCustomerCourses(email: str) -> List[Course]:
    """
        Returns all courses for a customer
    """
    return implementation.getCustomerCourses(email)

def purchase(customer_id: str, access_id: int) -> bool:
    """
        purchase a course access for a customer
    """
    return implementation.purchase(customer_id, access_id)
    