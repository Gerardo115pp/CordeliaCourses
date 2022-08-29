from .customers import CustomersRepository
from .courses import CoursesRepository
from .opinions import OpinionsRepository
from .mysql_utils import MYSQL_CONFIG

def createCustomersRepo() -> CustomersRepository:
    return CustomersRepository(MYSQL_CONFIG.createFromEnv())

def createCoursesRepo() -> CoursesRepository:
    return CoursesRepository(MYSQL_CONFIG.createFromEnv())

def createOpinionsRepo() -> OpinionsRepository:
    return OpinionsRepository(MYSQL_CONFIG.createFromEnv())