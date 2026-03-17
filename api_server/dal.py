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


def count_signal_type():
    query = """
        SELECT COUNT(*) as type_count, signal_type FROM intel_signals
            GROUP BY signal_type
            ORDER BY type_count DESC
        ;
    """
    result = client.execute_query(query)
    return result


def top_unidentified_entity():
    query = """
        SELECT COUNT(*) as appearances, entity_id FROM intel_signals
            WHERE priority_level = 99
            GROUP BY entity_id
            ORDER BY appearances DESC
            LIMIT 3
            ;
    """
    result = client.execute_query(query)
    return result


