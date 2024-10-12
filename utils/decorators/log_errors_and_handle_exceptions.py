from functools import wraps
from typing import Callable

from utils.decorators.clear_console import clear_console


def log_and_handle_exceptions(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            print(f"[ERROR] ValueError en {func.__name__}: {ve} \n")
            input("Presiona Enter para continuar...")
            clear_console()
            return None
        except Exception as e:
            print(f"[ERROR] Excepción general en {func.__name__}: {e} \n")
            input("Presiona Enter para continuar...")
            clear_console()
        return None
    return wrapper