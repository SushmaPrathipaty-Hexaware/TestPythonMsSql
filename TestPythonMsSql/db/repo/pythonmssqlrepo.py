from db.models.pythonmssql import Pythonmssql
from db.session import get_session


def get_pythonmssql():
    with get_session() as session:
        return session.query(Pythonmssql).all()

def insert_pythonmssql(pythonmssql):
    with get_session() as session:
        session.add(pythonmssql)
        session.commit()

def update_pythonmssql(id, schema_pythonmssql):
    with get_session() as session:
        pythonmssql = session.get(Pythonmssql, id)
        for key, value in schema_pythonmssql.items():
            setattr(pythonmssql, key, value)
        session.commit()

def delete_pythonmssql(id):
    with get_session() as session:
        pythonmssql = session.get(Pythonmssql, id)
        session.delete(pythonmssql)
        session.commit()
        
