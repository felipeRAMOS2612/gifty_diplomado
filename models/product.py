from datetime import datetime

class Product:
    def save(self, name: str, price: float, code: str, category: str, detail: str, stock: int, created_at: str):
        self.name = name
        self.price = price
        self.code = code
        self.category = category
        self.detail = detail
        self.created_at = created_at
        self.stock = stock
        return self
        
    def update(self, name=None, price=None, code=None, category=None, detail=None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if code is not None:
            self.code = code
        if category is not None:
            self.category = category
        if detail is not None:
            self.detail = detail
            
    def fifo(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        else:
            return False