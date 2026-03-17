import mysql.connector
from pprint import pprint

connection_config = {
      "host": "localhost",
      "port": 3307,
      "user": "root",
      "password": "root",
      "database": "digital_hunter"
    }
p = "kjSe#T53;G6n"
conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="digital_hunter"
)


class SqlConnection:
    def __init__(self):
        self.client = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="root",
            database="digital_hunter"
            )

    def execute_query(self, query: str):
        with self.client.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result


