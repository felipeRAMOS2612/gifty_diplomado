from datetime import datetime, timedelta
from models.inventory import Inventory


def get_low_stock(inventories: list[Inventory]) -> list[Inventory]:
    low_stock = []
    for inventory in inventories:
        if inventory.stock < 10:
            print(f"El inventario {inventory.name} Tiene bajo stock")
            print(f"Stock: {inventory.stock}\n")
    return low_stock


def total_stock(inventories: list[Inventory]) -> int:
    total = 0
    for inventory in inventories:
        total += inventory.stock
    return total

def total_inventories(inventories: list[Inventory]) -> int:
    return len(inventories)

def highest_value(inventories: list[Inventory]) -> Inventory:
    pass
    
def lowest_value(inventories: list[Inventory]) -> Inventory:
    pass

def inventories_recently_added(inventories: list[Inventory]) -> list[Inventory]:
    recently_added = []
    for inventory in inventories:
        if isinstance(inventory.created_at, datetime) and inventory.created_at + timedelta(days=3) >= datetime.now():
            recently_added.append(inventory)
    return recently_added