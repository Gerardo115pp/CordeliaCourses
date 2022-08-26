from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4
from typing import List, Dict, Any
import bcrypt

def allArgsPresent(obj: object, args: List[str]) -> bool:
    """ 
        this method should be reassigned from the __init__.py file
    """
    raise NotImplementedError("this shouldnt happen")

@dataclass
class Customer:
    
    id: str
    name: str
    last_name: str
    email: str
    last_item_check: float # timestamp
    google_code: str = ""
    password: str = ""
    
    @staticmethod
    def recreate(**kwargs) -> 'Customer':
        """ 
            creates a new customer object from the given kwargs, it expects all the fields to be present, if creating a new customer, use Customer.create() instead
        """
        assert allArgsPresent(Customer, kwargs), f"{kwargs} are not all present in Customer.create"
        assert kwargs['password'] or kwargs['google_code'], "password or google_code is required"
        
        new_customer = Customer(**kwargs)
        return new_customer
    
    @staticmethod
    def create(name: str, last_name: str, email: str, password:str="", google_code:str="") -> 'Customer':
        """ 
            creates a new customer object, it expects all the fields to be present, if creating a new customer, use Customer.create() instead
        """
        assert password or google_code, "password or google_code is required"
        
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        password = hashed.decode('utf-8')
        
        current_time = datetime.now()
        current_time = current_time.isoformat()
        
        customer_uuid = f"customer-{str(uuid4())}"
        new_customer = Customer(id=customer_uuid, name=name, last_name=last_name, email=email, password=password, google_code=google_code, last_item_check=current_time)
        return new_customer
        """ 
            creates a new customer object from the given kwargs, it expects only name, last_name, email and (password or google_code). it will set last time to current_time and generate a new id
        """
    
    def auth(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
        
    def changePassword(self, new_password: str) -> None:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(new_password.encode('utf-8'), salt)
        self.password = hashed.decode('utf-8')