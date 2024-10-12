def banner_gifty(func):
    def wrapper(*args, **kwargs):
        print("""
              ____ ___ _____ _______   __
             / ___|_ _|_   _|  ___\ \ / /
            | |  _ | |  | | | |_   \ V / 
            | |_| || |  | | |  _|   | |  
             \____|___| |_| |_|     |_|  
                                                                                                   
              """)
        print("=====================================================")
        print("   Bienvenido al sistema de gestion de inventario    ")
        print("-----------------------   ---------------------------")
        print("    Sistema desarrollado por equipo de trabajo 5     ")
        print("===================================================== \n")
        return func(*args, **kwargs)
    return wrapper