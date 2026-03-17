import mysql.connector

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

print(conn.is_connected())
with conn.cursor() as cursor:
    result = cursor.execute("USE digital_hunter; SHOW Tables;")
    print(conn)

    print(cursor)
print(result)