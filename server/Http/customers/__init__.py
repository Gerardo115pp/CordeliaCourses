from dataclasses import dataclass, asdict
from typing import List, Callable, Any, Dict
from inspect import getfullargspec

class RequestMeta(type):
    """
        A metaclass for requests
    """

    def __instancecheck__(cls, __instance: Any) -> bool:
        return cls.__subclasscheck__(type(__instance))

    def __subclasscheck__(cls, subclass: Any) -> bool:
        return (hasattr(subclass, 'fromDict') and callable(subclass.fromDict)) and \
                (hasattr(subclass, 'toDict') and callable(subclass.toDict))
                
class Request(metaclass=RequestMeta):
    """
        A interface for requests
    """
    @classmethod
    def fromDict(cls, dict: Dict[str, Any]) -> 'Request':
        """
            Initializes the request from a dict
        """
        raise NotImplementedError()
    
    def toDict(self) -> Dict[str, Any]:
        """
            Returns a dict representation of the request
        """
        raise NotImplementedError()
    
def createRequest(request_type: Request, args: Dict[str, Any]) -> Request:
    """
    Creates a request of the given type and initializes it with the given args, doesnt ensure that
    there are not extra args

    Parameters
    ----------
    request_type : Request
        request specific implementation
    args : Dict[str, Any]
        a dict with all the args needed to initialize the request

    Returns
    -------
    Request
        a request of the given type
    """
    
    # TODO: check why isinstance(request_type, Request) doesnt work, probably because of classmethod
    
    all_args = getfullargspec(request_type).args
    verifier:Callable = lambda a: a in all_args or a == "self" or a.startswith("_")
    are_all_present =  all(verifier(arg) for arg in args)
    if not are_all_present:
        return None
        
    return request_type.fromDict(args)

@dataclass
class CreatePasswordCustomerRequest:
    """
        A request to create a customer using a password instead of a google account
    """
    name: str
    last_name: str
    email: str
    password: str
    
    @classmethod
    def fromDict(cls, dict: Dict[str, Any]) -> 'CreatePasswordCustomerRequest':
        """
            Initializes the request from a dict
        """
        new_instance = cls(name=dict["name"], last_name=dict["last_name"], email=dict["email"], password=dict["password"])
        return new_instance

    def toDict(self) -> Dict[str, Any]:
        """
            Returns a dict representation of the request
        """
        return asdict(self)
    
@dataclass
class LoginPasswordCustomerRequest:
    """
        A request to login a customer using a password instead of a google account
    """
    email: str
    password: str
    
    @classmethod
    def fromDict(cls, dict: Dict[str, Any]) -> 'LoginPasswordCustomerRequest':
        """
            Initializes the request from a dict
        """
        new_instance = cls(email=dict["email"], password=dict["password"])
        return new_instance

    def toDict(self) -> Dict[str, Any]:
        """
            Returns a dict representation of the request
        """
        return asdict(self)
    