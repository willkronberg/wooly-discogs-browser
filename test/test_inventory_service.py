from typing import List
from src.services.inventory_service import InventoryService
from discogs_client.models import Release
from unittest.mock import Mock, patch
import pytest
from traceback import print_tb

secrets_mock = Mock()
discogs_mock = Mock()


class User:
    def __init__(self):
        self.collection_folders = []


@pytest.fixture
def discogs_response():
    return User()


@patch("src.services.inventory_service.SecretsService", secrets_mock)
@patch("src.services.inventory_service.Client", discogs_mock)
def test_get_inventory_with_consumer_token(discogs_response):
    discogs_mock.return_value.user.return_value = discogs_response

    response = None
    error = None
    try:
        inventory_service = InventoryService()
        response = inventory_service.get_inventory()
    except Exception as e:
        print(e)
        error = e
        raise e

    assert error is None
    assert response is not None
