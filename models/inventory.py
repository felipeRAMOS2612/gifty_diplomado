from datetime import datetime


class Inventory:
    def save(self, name, ubication, code, created_at, stock = 0, products = None):
        self.name = name
        self.ubication = ubication
        self.products = products if products is not None else []
        self.code = code
        self.stock = stock
        self.created_at = created_at

    def update(self, name=None, ubication=None):
        if name is not None:
            self.name = name
        if ubication is not None:
            self.ubication = ubication
    
    def add_products(self, product):
        self.products.append(product)
        
    def remove_products(self, product):
        self.products = [p for p in self.products if p["code"] != product.code]
        
    def list_products(self):
        return [product for product in self.products]
            
    def fifo(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        else:
            return False
    
    def increase_stock(self, quantity):
        self.stock += quantity
        return self.stock