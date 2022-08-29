from .mysql_utils import MysqlConnection, MYSQL_CONFIG
from typing import List, Dict
from models import Opinion

class OpinionsRepository:
    def __init__(self, config: MYSQL_CONFIG):
        self.config = config
        
    def getByClassCourse(self, class_id: str, course_id: int) -> List[Opinion]:
        """
            Returns all opinions by class and course
        """
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM opinions WHERE class_id = '{class_id}' AND course_id = '{course_id}'")
            rows = cursor.fetchall()
        return [Opinion(**row) for row in rows]


    def insert(self, opinion: Opinion) -> None:
        """
            Inserts a opinion
        """
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO opinions(`customer_id`, `class_id`, `course_id`, `username`, `body`, `isodate`) VALUES ('{opinion.customer_id}', '{opinion.class_id}', '{opinion.course_id}', '{opinion.username}', '{opinion.body}', '{opinion.isodate}')")
            conn.commit()
        return