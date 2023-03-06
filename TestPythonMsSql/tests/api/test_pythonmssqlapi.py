import json
import unittest
from unittest import mock
from fastapi.testclient import TestClient
from api.routes import app
from schema.pythonmssql import Pythonmssql
from core.logger import logger

ENDPOINT = '/pythonmssql'
SUCCESS_MSG = '"success"'


class TestPythonmssqlAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.pythonmssql = {
            'id': 1,
            'name': '6PrXs'
        }
        self.pythonmssql_list = [self.pythonmssql]
        self.client = TestClient(app)
        logger.disabled = True

    @mock.patch('api.pythonmssqlapi.pythonmssqlservice.fetch_pythonmssql')
    def test_api_fetch_pythonmssql(self, mock_fetch):

        mock_fetch.return_value = self.pythonmssql_list

        response = self.client.get(ENDPOINT)
        response_content = json.loads(response.content.decode('utf-8'))

        assert response.status_code == 200
        assert response_content == self.pythonmssql_list

    @mock.patch('api.pythonmssqlapi.pythonmssqlservice.insert_pythonmssql')
    def test_api_insert_pythonmssql(self, mock_insert):

        mock_insert.return_value = self.pythonmssql_list
        pythonmssql = Pythonmssql(**self.pythonmssql)
        print(pythonmssql)

        response = self.client.post(ENDPOINT, data = json.dumps(self.pythonmssql))
        response_content = response.content.decode('utf-8')

        assert response_content == SUCCESS_MSG
        assert mock_insert.called

    @mock.patch('api.pythonmssqlapi.pythonmssqlservice.update_pythonmssql')
    def test_api_update_pythonmssql(self, mock_update):

        mock_update.return_value = self.pythonmssql_list

        response = self.client.put(f'{ENDPOINT}/1', data = json.dumps(self.pythonmssql))
        response_content = response.content.decode('utf-8')

        assert response_content == SUCCESS_MSG
        assert mock_update.called

    @mock.patch('api.pythonmssqlapi.pythonmssqlservice.delete_pythonmssql')
    def test_api_delete_pythonmssql(self, mock_delete):

        mock_delete.return_value = self.pythonmssql_list

        response = self.client.delete(f'{ENDPOINT}/1')
        response_content = response.content.decode('utf-8')

        assert response.status_code == 200
        assert response_content == SUCCESS_MSG
        assert mock_delete.called
