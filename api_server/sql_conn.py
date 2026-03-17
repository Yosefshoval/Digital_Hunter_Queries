import mysql.connector
from pprint import pprint
import os

class SqlConnection:
    def __init__(self):
        self.client = mysql.connector.connect(
            host=os.getenv("SQL_HOST", "localhost"),
            port=int(os.getenv("SQL_PORT", "3307")),
            user=os.getenv("SQL_USERNAME", "root"),
            password=os.getenv("SQL_PASSWORD", "root"),
            database=os.getenv("SQL_DATABASE", "digital_hunter")
            )

    def execute_query(self, query: str):
        with self.client.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result


