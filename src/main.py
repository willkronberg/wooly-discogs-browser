from src.services import inventory_service

try:
    message = inventory_service.get_inventory()
    print(f"Your IP Address is: {message}")
except Exception as e:
    print("An Unexpected Exception Has Occurred!")
    print(e)
