from schema import pythonmssql as SchemaPythonmssql
from db.models.pythonmssql import Pythonmssql
from db.repo import pythonmssqlrepo


def fetch_pythonmssql():
    return pythonmssqlrepo.get_pythonmssql()

def insert_pythonmssql(schema_pythonmssql):
    pythonmssql = Pythonmssql(**schema_pythonmssql.dict())
    pythonmssqlrepo.insert_pythonmssql(pythonmssql)

def update_pythonmssql(id, schema_pythonmssql):
    pythonmssql = schema_pythonmssql.dict()
    del pythonmssql['id']
    pythonmssqlrepo.update_pythonmssql(id, pythonmssql)

def delete_pythonmssql(id):
    pythonmssqlrepo.delete_pythonmssql(id)