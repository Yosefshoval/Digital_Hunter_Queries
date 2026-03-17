from sql_conn import SqlConnection

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
            entity_id, 
            SUM(distance_from_last) as distance,
            timestamp
        FROM 
            (
            SELECT * FROM intel_signals
            WHERE 
                HOUR(timestamp) BETWEEN 8 AND 20
                OR ((HOUR(timestamp) BETWEEN 20 AND 24) OR (HOUR(timestamp) BETWEEN 0 AND 8))
            ) t1
        GROUP BY entity_id, timestamp             
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


def find_bonding_events():
    query = """
        SELECT * FROM intel_signals
        WHERE distance >= 1
            AND entity1 = 99 AND entity2 = 1
    """


""".הפיזי והמרחק מפגש זמן ,entity_id_asset, entity_id_prority """