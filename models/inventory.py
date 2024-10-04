class Inventory:
    def save(self, name, ubication, products = []):
        self.name = name
        self.ubication = ubication
        self.products = products

    def update(self, name=None, ubication=None):
        if name is not None:
            self.name = name
        if ubication is not None:
            self.ubication = ubication
    
    def add_products(self, product):
        self.products.append(product)
        
    def remove_products(self, product):
        self.products = product
        
    def list_products(self):
        for product in self.products:
            print(product.name)