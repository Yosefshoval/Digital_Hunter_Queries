from fastapi import APIRouter
from dal import *
import mysql.connector.errors as sql_err


router = APIRouter()

@router.get('/query/top-level')
def get_top_level():
    try:
        return top_level()
    except (sql_err.ProgrammingError, sql_err.Error) as e:
        pprint(e)
