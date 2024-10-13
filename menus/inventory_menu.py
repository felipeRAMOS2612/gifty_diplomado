

from services.inventory_service import *
from menus.product_menu import products

inventories = []


def inventory_menu():
    options: dict = {
        1: handle_create_inventory,
        2: handle_list_inventories,
        3: handle_update_inventory,
        4: handle_add_item,
        5: handle_sell_product,
        6: lambda: None
    }
    while True:
        print("1. Crear inventario")
        print("2. Listar inventarios")
        print("3. Actualizar inventario")
        print("4. Añadir producto a inventario")
        print("5. Eliminar producto de inventario")
        print("6. Volver atras \n")
        option = int(input("Elige una opción: "))
        
        if option in options:
            if option == 6:
                break
            options[option]()
        else:
            print("Opción no válida")
        
def handle_create_inventory():
    create_inventory(inventories)
    
def handle_list_inventories():
    list_inventories(inventories)
    
def handle_update_inventory():
    update_inventory(inventories)
    
def handle_add_item():
    add_item(inventories, products)
    
def handle_sell_product():
    sell_product(inventories)