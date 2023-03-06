import unittest
from unittest import mock
from schema.pythonmssql import Pythonmssql as PythonmssqlSchema
from api.routes import app
from business import pythonmssqlservice

ENDPOINT = '/pythonmssql'
SUCCESS_MSG = '"success"'


class TestPythonmssqlService(unittest.TestCase):

    def setUp(self) -> None:
        self.pythonmssql = {
            'id': 1,
            'name': 'xd80u'
        }
        self.pythonmssql_list = [self.pythonmssql]
        self.pythonmssql_schema_obj = PythonmssqlSchema(**self.pythonmssql)
    
    @mock.patch('business.pythonmssqlservice.pythonmssqlrepo.get_pythonmssql')
    def test_fetch_pythonmssql(self, mock_fetch):

        mock_fetch.return_value = self.pythonmssql_list

        out = pythonmssqlservice.fetch_pythonmssql()
        
        assert out == self.pythonmssql_list
        assert mock_fetch.called

    @mock.patch('business.pythonmssqlservice.pythonmssqlrepo.insert_pythonmssql')
    def test_api_insert_pythonmssql(self, mock_insert):

        mock_insert.return_value = None

        out = pythonmssqlservice.insert_pythonmssql(self.pythonmssql_schema_obj)
        
        assert mock_insert.called
        assert out == None


    @mock.patch('business.pythonmssqlservice.pythonmssqlrepo.update_pythonmssql')
    def test_api_update_pythonmssql(self, mock_update):

        mock_update.return_value = None

        out = pythonmssqlservice.update_pythonmssql(1, self.pythonmssql_schema_obj)
        
        assert mock_update.called
        assert out == None

    @mock.patch('business.pythonmssqlservice.pythonmssqlrepo.delete_pythonmssql')
    def test_api_delete_pythonmssql(self, mock_delete):

        mock_delete.return_value = None

        out = pythonmssqlservice.delete_pythonmssql(1)
        
        assert mock_delete.called
        assert out == None
