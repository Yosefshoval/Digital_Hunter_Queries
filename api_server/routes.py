from fastapi import APIRouter
from dal import *
import mysql.connector.errors as sql_err
from api_server.maps_data import DigitalHunter_map

router = APIRouter()

exceptions = (sql_err.ProgrammingError, sql_err.Error, sql_err.DatabaseError)

@router.get('/query/top-level')
def get_top_level():
    try:
        return top_level()
    except exceptions as e:
        pprint(e)


@router.get('/query/count-signal-type')
def get_count_signal_type():
    try:
        return count_signal_type()
    except exceptions as e:
        pprint(e)


@router.get('/query/top-unidentified-entity')
def get_top_unidentified_entity():
    try:
        return top_unidentified_entity()
    except exceptions as e:
        pprint(e)

@router.get('/query/waked-up-targets')
def get_waked_up_targets():
    try:
        return waked_up_targets()
    except exceptions as e:
        pprint(e)


@router.get('/route-of-target/{target_id}')
def get_route(target_id: str):
    coords = get_coords_by_id(target_id)
    if not coords:
        return "target_id not found"

    points = []
    for record in coords:
        c = tuple(record.values())
        c1, c2 = float(str(c[1])[:5]), float(str(c[0])[:5])
        points.append((c1, c2))
    DigitalHunter_map.plot_map_with_geometry(points)
    return "success"

get_route('TGT-007')