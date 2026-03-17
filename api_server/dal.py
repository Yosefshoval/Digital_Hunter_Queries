from sql_conn import SqlConnection
from pprint import pprint

client = SqlConnection()



def top_level():
    query = ("SELECT entity_id, target_name, priority_level, movement_distance_km FROM targets "
             "WHERE priority_level IN (1, 2) "
             "AND movement_distance_km > 5"
             ";")
    result = client.execute_query(query)
    return result


