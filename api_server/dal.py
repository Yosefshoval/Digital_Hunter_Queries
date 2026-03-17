from sql_conn import SqlConnection
import DigitalHunter_map

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


def waked_up_targets():
    query = """
        SELECT 
            intel_signals.entity_id, 
            SUM(intel_signals.distance_from_last) as distance, 
            
        FROM intel_signals
        JOIN attacks 
            ON intel_signals.entity_id = attacks.entity_id
        WHERE 
            intel_signals.timestamp <= DATE_SUB(attacks.timestamp, INTERVAL 3 hour)
            AND intel_signals.timestamp >= DATE_SUB(attacks.timestamp, INTERVAL 3 hour)
        
        GROUP BY intel_signals.entity_id
        HAVING distance = 0
        OR distance >= 10
        ;
    """
    result = client.execute_query(query)
    return result



def get_coords_by_id(target_id: str):
    query = f"""
    SELECT reported_lat, reported_lon FROM intel_signals
    WHERE entity_id = '{target_id}';
    """
    result = client.execute_query(query)
    return result



