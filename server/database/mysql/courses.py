from .mysql_utils import MysqlConnection, MYSQL_CONFIG
from typing import List, Dict
from models import Course

class CoursesRepository:
    def __init__(self, config: MYSQL_CONFIG):
        self.config = config
        
    def count(self) -> int:
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM courses")
            row = cursor.fetchone()
            
        return row[0] if row else 0
        
    def getAll(self) -> List[Course]:
        courses = []
        
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM courses")
            rows = cursor.fetchall()
        
        courses = [Course.create(**row) for row in rows]
        return courses

    def getById(self, id: str) -> Course:
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM courses WHERE id = '{id}'")
            row = cursor.fetchone()
            
        return Course.create(**row) if row else None

    def getSpecialAccessMap(self) -> Dict[int, str]:
        special_access_map: Dict[int, str] = {}
        
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT `a`.`product_id` as `id`, `c`.`course_data` FROM `accesses` `a` LEFT JOIN `courses` `c` ON `a`.`course_id`=`c`.`id` WHERE `a`.`name`='special-access';")
            rows = cursor.fetchall()
        
        special_access_map = {row['id']: row['course_data'] for row in rows}
        return special_access_map

    def getCustomerCourses(self, email: str) -> Dict:
        sql = f"SELECT * FROM `courses` WHERE `id` IN (SELECT `accesses`.`course_id` FROM `purchases`, `accesses` WHERE `accesses`.`product_id`=`purchases`.`access_id` AND `purchases`.`customer_id`=(SELECT `id` FROM `customers` WHERE `email`='{email}'));"
        
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            rows = cursor.fetchall()
        
        return [Course.recreate(**row) for row in rows]
    
    def purchase(self, customer_id: str, access_id: int) -> bool:
        sql = f"INSERT INTO `purchases` (`customer_id`, `access_id`) VALUES ('{customer_id}', {access_id});"
        
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            try:
                conn.commit()
                return True
            except Exception as e:
                print(f"WARNING: {e}")
                return False
                