from .mysql_utils import MysqlConnection, MYSQL_CONFIG
from typing import List, Dict
from models import Customer

class CustomersRepository:
    def __init__(self, config: MYSQL_CONFIG):
        self.config = config
    
    def getAll(self) -> Dict[str, Customer]:
        customers_lookup = {}
        
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM customers")
            rows = cursor.fetchall()
        
        customers_lookup = {row['email']: Customer(**row) for row in rows}
        return customers_lookup
    
    def insert(self, customer: Customer) -> None:
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO customers VALUES ('{customer.id}', '{customer.name}', '{customer.last_name}', '{customer.google_code}', '{customer.password}', '{customer.email}', '{customer.last_item_check}')")
            conn.commit()
            
    def getByEmail(self, email: str) -> Customer:
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM customers WHERE email = '{email}'")
            row = cursor.fetchone()
            
        return Customer.recreate(**row) if row else None
    
    def getById(self, id: str) -> Customer:
        with MysqlConnection(self.config) as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM customers WHERE id = '{id}'")
            row = cursor.fetchone()
            
        return Customer.create(**row) if row else None