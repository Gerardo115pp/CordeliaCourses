from typing import List, Dict, Any
from models import Customer

class CustomersRepoMeta(type):
    """ 
        A metaclass for customers repository
    """
    
    def __instancecheck__(cls, __instance: Any) -> bool:
        return cls.__subclasscheck__(type(__instance))
    
    def __subclasscheck__(cls, subclass: Any) -> bool:
        return (hasattr(subclass, 'getAll') and  callable(subclass.getAll)) and \
                (hasattr(subclass, 'insert') and  callable(subclass.insert)) and \
                (hasattr(subclass, 'getByEmail') and  callable(subclass.getByEmail)) and \
                (hasattr(subclass, 'getById') and  callable(subclass.getById))
                
class CustomersRepo(metaclass=CustomersRepoMeta):
    """
        A interface for customers repository
    """
    
    def getAll(self) -> Dict[str, Customer]:
        """
            Returns all customers {email: customer}
        """
        raise NotImplementedError()
    
    def insert(self, customer: Customer) -> None:
        """
            Inserts a customer
        """
        raise NotImplementedError()
    
    def getByEmail(self, email: str) -> Customer:
        """
            Returns a customer by email
        """
        raise NotImplementedError()
    
    def getById(self, id: str) -> Customer:
        """
            Returns a customer by id
        """
        raise NotImplementedError()
    
    
implementation: CustomersRepo = None

def setRepository(repo: CustomersRepo) -> None:
    """
        Sets the customers repository
    """
    global implementation
    assert isinstance(repo, CustomersRepo), f"{repo} is not an instance of CustomersRepo"
    implementation = repo
    
def getAll() -> Dict[str, Customer]:
    """
        Returns all customers {email: customer}
    """    
    return implementation.getAll()

def insert(customer: Customer) -> None:
    implementation.insert(customer)
    
def getByEmail(email: str) -> Customer:
    return implementation.getByEmail(email)

def getById(id: str) -> Customer:
    return implementation.getById(id)