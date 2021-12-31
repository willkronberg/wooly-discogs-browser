from src.services.inventory_service import InventoryService


def test_get_inventory_with_consumer_token():
    message = None
    error = None

    try:
        inventory_service = InventoryService()
        message = inventory_service.get_inventory()
    except Exception as e:
        print(e)
        error = e

    assert error is None
    assert message == "hello, world"
