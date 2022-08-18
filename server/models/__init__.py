from . import Customer as customer_module
from . import Course as course_module
from inspect import getfullargspec
from typing import List

def _allArgsPresent(obj: object, args: List[str]) -> bool:
    all_args = getfullargspec(obj).args
    are_all_present =  all(arg in all_args or arg == "self" for arg in args)
    if not are_all_present:
        print(f"({args}) are not all present in ({all_args})")
        
    return are_all_present

# CUSTOMER
customer_module.allArgsPresent = _allArgsPresent # reassign the method 
Customer = customer_module.Customer # reassign the class, cleaner imports

# COURSE
course_module.allArgsPresent = _allArgsPresent # reassign the method
Course = course_module.Course # reassign the class, cleaner imports