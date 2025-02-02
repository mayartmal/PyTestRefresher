import pytest
import unittest.mock as mock

import requests

import source.service
import source.service as service


@mock.patch("source.service.get_user_from_db")
def test_get_used_from_db(mocked_get_user_from_db):
    mocked_get_user_from_db.return_value = "Mocked Artem" #подмена значения из db
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Artem"
    #assert user_name == "Artem"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200 #это просто свойство, которое ничего не вызывает, поэтому тут нет return_value
    mock_response.json.return_value = {"id": 1, "name": "John Doe"} #а уже это предполагет возврат значения после вызова
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}

@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()