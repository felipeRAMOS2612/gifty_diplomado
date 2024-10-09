from models.product import Product
from models.inventory import Inventory
from models.user import User

def menu():
    print("Bienvenido al sistema de inventario")
    print("1. Añadir producto")
    print("2. Añadir inventario")
    print("3. Exit")
    try:
        option = int(input("Elige una opción: "))
        return option
    except ValueError:
        print("Opción tiene que ser un numero")

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
    
def main():
    while True:
        option = menu()
        if option == 1:
            add_product()
        elif option == 2:
            add_inventory()
        elif option == 3:
            print("Hasta luego")
            break
        else:
            print("Opción no válida")
            
if __name__ == "__main__":
    main()