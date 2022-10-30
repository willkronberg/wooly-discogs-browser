from src.services.inventory_service import InventoryService
from discogs_client.models import Release


def test_get_inventory_with_consumer_token():
    response = None
    error = None
    try:
        inventory_service = InventoryService()
        response = inventory_service.get_inventory()
    except Exception as e:
        print(e)
        error = e

    assert error is None
    assert len(response) > 0
    assert type(response[0]) is Release
