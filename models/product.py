class Product:
    def save(self, name, price, code, category, detail):
        self.name = name
        self.price = price
        self.code = code
        self.category = category
        self.detail = detail
        
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
            