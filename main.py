from models.product import Product
from models.inventory import Inventory
from models.user import User

def menu():
    print("Bienvenido al sistema de inventario")
    print("1. Añadir producto")
    print("2. Añadir inventario")
    print("3. Exit")
    option = int(input("Elige una opción: "))
    if(option < 1 or option > 3 or option == None):
        print("Opción no válida")
        return menu()
    return option

def add_product():
    name = input("Nombre del producto: ")
    price = input("Precio del producto: ")
    code = input("Código del producto: ")
    category = input("Categoría del producto: ")
    detail = input("Detalle del producto: ")
    product = Product()
    product.save(name, price, code, category, detail)
    print("Producto añadido correctamente")
    print(product.name)
    
def add_inventory():
    name = input("Nombre del inventario: ")
    ubication = input("Ubicación del inventario: ")
    inventory = Inventory()
    inventory.save(name, ubication)
    print("Inventario añadido correctamente")
    
def exit():
    return False
    
def main():
    option = menu()
    if option == 1:
        add_product()
    elif option == 2:
        add_inventory()
    elif option == 3:
        print("Hasta luego")
        exit()
    else:
        print("Opción no válida")
        main()


while True:
    if(not main()):
        break