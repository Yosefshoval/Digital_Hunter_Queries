from fastapi import APIRouter
from dal import *
import mysql.connector.errors as sql_err

router = APIRouter()

exceptions = (sql_err.ProgrammingError, sql_err.Error)

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

