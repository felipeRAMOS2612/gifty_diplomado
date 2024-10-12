from services.product_service import *

products = []

def product_menu():
    options:dict = {
        1: handle_create_product,
        2: handle_list_products,
        3: handle_update_product,
        4: handle_find_product,
        5: lambda: None
    }
    
    while True:
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Buscar producto especifico")
        print("5. Volver atras \n")
        option = int(input("Elige una opción: "))
        
        if option in options:
            if option == 5:
                break
            options[option]()
        else:
            print("Opción no válida")

        
def handle_create_product():
    create_product(products)

def handle_list_products():
    list_products(products)
    
def handle_update_product():
    update_product(products)
    
def handle_find_product():
    find_product(products)
    
