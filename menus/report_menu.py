from services.report_service import *
from menus.inventory_menu import inventories
from utils.decorators.clear_console import clear_console

def report_menu():
    while True:
        clear_console()
        print("Reporte de inventario: \n")
        print("=============== Inventarios con bajo stock ===============")
        handle_get_low_stock()
        print("=============== Inventarios recientemente agregados ===============")
        handle_recently_added()
        print("=============== Total de stock ===============")
        print(f"\n Stock total: {handle_total_stock()}")
        print("=============== Total de inventarios ===============")
        print(f"\n Total de inventarios: {handle_total_inventories()}")
        
        input("\nPresiona enter para continuar... ")
        break
    
    
def handle_get_low_stock():
    low_stock = get_low_stock(inventories)
    for inventory in low_stock:
        print("Inventario:", inventory)
        print(f"--------- Inventario {inventory.name} ---------")
        print(f"\n Stock: {inventory.stock}")
        print(f"Ubicación: {inventory.ubication}\n")
    
def handle_recently_added():
    recently_added = inventories_recently_added(inventories)
    for inventory in recently_added:
        print(f"--------- Inventario {inventory.name} ---------")
        print(f"\n Stock: {inventory.stock}")
        print(f"Ubicación: {inventory.ubication}\n")
    
def handle_total_stock():
    return total_stock(inventories)
    
def handle_total_inventories():
    return total_inventories(inventories)
    
def handle_highest_value():
    highest_value(inventories)
    
def handle_lowest_value():
    lowest_value(inventories)