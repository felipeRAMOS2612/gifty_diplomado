class User:
    def save(self, name, dni, phone, address):
        self.name = name
        self.dni = dni
        self.phone = phone
        self.address = address
    
    def update(self, name=None, dni=None, phone=None, address=None):
        if name is not None:
            self.name = name
        if dni is not None:
            self.dni = dni
        if phone is not None:
            self.phone = phone
        if address is not None:
            self.address = address