from datetime import datetime
from models.inventory import Inventory
from models.product import Product
from services.product_service import find_product, find_by_code
from menus.product_menu import products
from utils.decorators.log_errors_and_handle_exceptions import log_and_handle_exceptions

@log_and_handle_exceptions
def create_inventory(inventories: list[Inventory]):
    name = input("Nombre: ")
    ubication = input("Ubicación: ")
    code = int(input("Codigo: "))
    if verify_code(inventories, code):
        print("El código ya existe.")
        return None
    inventory = Inventory()
    inventory.save(name=name, ubication=ubication, code=code, created_at=datetime.now())
    inventories.append(inventory)
    print("Inventario creado con exito")
    
def verify_code(inventories: list[Inventory], code: str) -> bool:
    for inventory in inventories:
        if inventory.code == code:
            return True
    return False
    
@log_and_handle_exceptions
def list_inventories(inventories: list[Inventory]):
    for inventory in inventories:
        print(f"Nombre: {inventory.name}")
        print(f"Ubicación: {inventory.ubication}")
        print(f"Codigo: {inventory.code}")
        print(f"Stock: {inventory.stock}")
        print(f"Fecha de creación: {inventory.created_at}")
        if inventory.products:
            product_names = [
                prod.name 
                for product_dict in inventory.products 
                for prod in products if prod.code == product_dict["code"]
            ]
            print(f"Productos: {', '.join(product_names) if product_names else 'Ninguno'}")
        print("-------------------------------")

@log_and_handle_exceptions
def find_inventory(inventories: list[Inventory]):
    code = input("Código del inventario: ")
    for inventory in inventories:
        if str(inventory.code) == code:
            return inventory
    print("Inventario no encontrado.")
    return None

@log_and_handle_exceptions
def update_inventory(inventories: list[Inventory]):
    inventory = find_inventory(inventories)
    if not inventory:
        return

    print("1. Nombre")
    print("2. Ubicación")
    option = int(input("Elige una opción: "))

    if option == 1:
        name = input("Nuevo nombre: ")
        inventory.update(name=name)
    elif option == 2:
        ubication = input("Nueva ubicación: ")
        inventory.update(ubication=ubication)
    else:
        print("Opción no válida.")
    print("Inventario actualizado con éxito.")
      
@log_and_handle_exceptions  
def add_item(inventories: list[Inventory], products: list[Product]):
    inventory: Inventory = find_inventory(inventories)
    if not inventory:
        return

    product: Product = find_product(products)
    if not product:
        print("Producto no encontrado.")
        return
    inventory.add_products({"code": product.code, "added_at": datetime.now()})
    inventory.increase_stock(product.stock)
    print("Producto añadido al inventario.")
    
@log_and_handle_exceptions
def sell_product(inventories):
    inventory: Inventory = find_inventory(inventories)
    if not inventory:
        return
    inventory_products = [
        prod for product_dict in inventory.products 
        for prod in products if prod.code == product_dict["code"]
    ]
    product: Product  = find_product(inventory_products)
    quantity = int(input("Cantidad: "))
    if quantity < 0:
        print("La cantidad no puede ser negativa.")
        return
    if inventory.fifo(quantity) and product.fifo(quantity):
        if product.stock == 0:
            inventory.remove_products(product)
        print("Cantidad restada del stock.")
    else:
        print("No hay suficiente stock.")
    