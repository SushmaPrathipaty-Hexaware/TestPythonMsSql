import traceback
from fastapi import APIRouter, HTTPException
from business import pythonmssqlservice
from schema.pythonmssql import Pythonmssql

router = APIRouter(prefix="/pythonmssql")


@router.get('')
def api_fetch_pythonmssql():
    return pythonmssqlservice.fetch_pythonmssql()

@router.post('')
def api_insert_pythonmssql(pythonmssql: Pythonmssql):
    pythonmssqlservice.insert_pythonmssql(pythonmssql)
    return "success"

@router.put('/{id}')
def api_update_pythonmssql(id: int, pythonmssql: Pythonmssql):
    pythonmssqlservice.update_pythonmssql(id, pythonmssql)
    return "success"

@router.delete('/{id}')
def api_delete_pythonmssql(id: int):
    pythonmssqlservice.delete_pythonmssql(id)
    return "success"