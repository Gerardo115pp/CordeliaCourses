from .customers import CustomersRepository
from .courses import CoursesRepository
from .mysql_utils import MYSQL_CONFIG

def createCustomersRepo() -> CustomersRepository:
    return CustomersRepository(MYSQL_CONFIG.createFromEnv())

def createCoursesRepo() -> CoursesRepository:
    return CoursesRepository(MYSQL_CONFIG.createFromEnv())