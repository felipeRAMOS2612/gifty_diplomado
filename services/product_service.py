from datetime import datetime
from models.product import Product
from utils.decorators.log_errors_and_handle_exceptions import log_and_handle_exceptions

def categories() -> dict:
    return {
        "1": "Empaque y Envoltura",
        "2": "Accesorios",
        "3": "Juguetería",
        "4": "Decoración",
        "5": "Papelería"
    }

@log_and_handle_exceptions
def create_product(products)-> Product:
    name = input("Nombre: ")
    price = float(input("Precio: "))
    code = input("Codigo: ")
    code = code.upper()
    if verify_code(products, code):
        print("El código ya existe.")
        return None
    print("Categorías: \n")
    
    for key, value in categories().items():
        print(f"{key}: {value}")
    
    category_key = input("\nCategoria por numero de la lista: ")
    category = categories().get(category_key, "not validate")
    if category == "not validate":
        print("Categoría no válida seleccionada.")
        return None
    detail = input("Detalle: ")
    stock = int(input("Stock: "))
    created_at = datetime.now()
    product = Product()
    product_saved = product.save(name=name, price=price, code=code, detail=detail, category=category, created_at=created_at, stock=stock)
    products.append(product_saved)
    print("Producto creado con exito")
    return product_saved

def verify_code(products: list[Product], code: str) -> bool:
    for product in products:
        if product.code == code:
            return True
    return False
  
@log_and_handle_exceptions  
def list_products(products):
    print("-------------------------------")
    print("Historial de productos: ")    
    for product in products:
        print(f"Nombre: {product.name}")
        print(f"Precio: {product.price}")
        print(f"Codigo: {product.code}")
        print(f"Categoria: {product.category}")
        print(f"Detalle: {product.detail}")
        print(f"Fecha de creación: {product.created_at}")
        print(f"Stock: {product.stock}")
        print("-------------------------------")
    return products
    
@log_and_handle_exceptions
def find_product(products: list[Product]) -> Product:
    code = input("Codigo del producto: ")
    for product in products:
        if str(product.code) == code:
            print("\n Producto encontrado: \n")
            print(f"Nombre: {product.name}")
            print(f"Precio: {product.price}")
            print(f"Codigo: {product.code}")
            print(f"Categoria: {product.category}")
            print(f"Detalle: {product.detail}")
            print(f"Fecha de creación: {product.created_at}")
            print("------------------------------- \n")
            return product
    return None

@log_and_handle_exceptions
def find_by_code(products: list[Product], code: str) -> Product:
    for product in products:
        if product.code == code:
            return product
    return None
   
@log_and_handle_exceptions     
def update_product(products) -> Product:
    product = find_product(products)

    if not product:
        return

    print("\n ¿Qué deseas actualizar? \n")
    print("1. Nombre")
    print("2. Precio")
    print("3. Categoría")
    print("4. Detalle")
    option = int(input("Elige una opción: "))

    if option == 1:
        name = input("Nuevo nombre: ")
        product.update(name=name)
    elif option == 2:
        price = float(input("Nuevo precio: "))
        product.update(price=price)
    elif option == 3:
        category = input("Nueva categoría: ")
        product.update(category=category)
    elif option == 4:
        detail = input("Nuevo detalle: ")
        product.update(detail=detail)
    else:
        print("Opción no válida.")
        
    print("Producto actualizado con éxito.")
    return product