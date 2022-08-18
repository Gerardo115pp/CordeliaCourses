from typing import List, Dict, Set
import repository
from Http.woocommerce import getEmailOrdersIds
import models
import requests
import json
import os


def createCustomerAccesses(customer: models.Customer, special_access_map: Dict[int, str]) -> None:
    """
        creates the customer accesses for the customer with the given email.
    """
    customer_accesses = getCustomerAccess(customer.email, special_access_map)
    print(f"{customer.email} has bought {len(customer_accesses)} accesses")
    for access_id in customer_accesses:
        repository.courses.purchase(customer.id, access_id)
        print(f"{customer.email} has access to {access_id}")
        
    return

# TODO: define a return type for this function
def getCustomerAccess(email: str, special_acceses: Dict[int, Set[str]]) -> None:
    """
        Checks all the accesses a customer has, each access grants a single course so if courses.length != customer_access.length then 
        its not necessary to check woocommerce.
    """
    customer_accesses = []
    
    # getting special access for the customer
    for course_id, special_accesses in special_acceses.items():
        if email in special_accesses:
            customer_accesses.append(course_id)
    
    # getting orders bought through woocommerce
    course_count = repository.courses.count()
    if len(customer_accesses) < course_count:
        woo_purshased_accesses = getEmailOrdersIds(email)
        customer_accesses += woo_purshased_accesses
    
    return customer_accesses
    
    
    
    

def getAccessFromFile(special_access_map: Dict[int, str]) -> Dict[str, Set[str]]:
    """ 
        get a dict mapping course id to its course_data which is the directory where its data
        is stored, for each course_data it reads the special_access.json file and creates
        a map course_id -> special_accesses[customer_email]. any customer with in that list
        has access to the course no need to check woocommerce.
    """
    courses_special_access = {}
    
    for course_id, course_directory in special_access_map.items():
        special_access_file = os.path.join(course_directory, "special_access.json")
        
        # if there is no special access file, continue
        if not os.path.exists(special_access_file):
            print(f"WARNING: {special_access_file} does not exist")
            continue
        
        # read course special access
        with open(special_access_file, "r") as f:
            acceses = json.load(f)
        
        courses_special_access[course_id] = set(acceses)
    
    return courses_special_access
            