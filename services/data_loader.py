from datetime import datetime
import json
from models.inventory import Inventory
from models.product import Product
from menus.inventory_menu import inventories
from menus.product_menu import products

def load_data_from_json(file_path: str) -> dict:
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {file_path}.")
        return {}
    
def load_products_from_json(data):
    for product_data in data["products"]:
        product = Product()
        product.save(
            name=product_data["name"],
            price=product_data["price"],
            code=str(product_data["code"]),
            category=product_data["category"],
            detail=product_data["detail"],
            stock=product_data["stock"],
            created_at=product_data["created_at"]
        )
        products.append(product)
    return products

def load_inventories_from_json(data, products):
    for inventory_data in data["inventories"]:
        inventory = Inventory()
        created_at = datetime.strptime(inventory_data['created_at'], '%Y-%m-%d')
        inventory.save(
            name=inventory_data["name"],
            ubication=inventory_data["ubication"],
            code=inventory_data["code"],
            created_at=created_at
        )
        inventories.append(inventory)
    return inventories