

class Cliente:
    def __init__(self, telefono, direccion, clientes):
        self.__telefono = telefono
        self.__direccion = direccion
        self.__clientes = clientes

    def get_telefono(self):
        return self.__telefono
    
    def get_direccion(self):
        return self.__direccion
    
    def get_clientes(self):
        return self.__clientes
    
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_direccion(self, direccion):
        self.__direccion = direccion
    
    def set_clientes(self, clientes):
        self.__clientes = clientes

    def __str__(self): 
        return f"Teléfono: {self.__telefono}, Dirección: {self.__direccion}, Clientes: {self.__clientes}"
    
    

