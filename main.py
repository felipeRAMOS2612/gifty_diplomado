from menus.report_menu import report_menu
from menus.inventory_menu import inventory_menu
from menus.product_menu import product_menu
from menus.report_menu import report_menu
from services.data_loader import *
from utils.decorators.clear_console import clear_console
from utils.decorators.banner_gifty import banner_gifty
from utils.decorators.log_errors_and_handle_exceptions import log_and_handle_exceptions


@banner_gifty
@log_and_handle_exceptions
def menu() -> int:
    options: dict = {
        1: inventory_menu,
        2: product_menu,
        3: report_menu,
        4: lambda: None
    }
    
    print("1. Gestion de inventario")
    print("2. Gestion de productos")
    print("3. Generar reporte")
    print("4. Salir \n")
    option = int(input("Elige una opción: "))
    if option in options:
        return option
    else:
        print("\n Tiene que elegir una opción válida")
        return menu()
    
def main() -> int:
    while True:
        clear_console()
        option = menu()
        if option == 1:
            inventory_menu()
        elif option == 2:
            product_menu()
        elif option == 3:
            report_menu()
        elif option == 4:
            print("\n Hasta luego")
            break
            
if __name__ == "__main__":
    data = load_data_from_json("./utils/data/data.json")
    products = load_products_from_json(data)
    inventories = load_inventories_from_json(data, products)
    main()