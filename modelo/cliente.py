from modelo.persona import Persona

class Cliente(Persona):
    def __init__(self, run="", nombre="", apellido="", direccion="", telefono=""):
        super().__init__(run, nombre, apellido) # Herencia explícita
        self.__direccion = direccion
        self.__telefono = telefono

    # Getters y Setters
    def getDireccion(self): return self.__direccion
    def getTelefono(self): return self.__telefono
    def setDireccion(self, d): self.__direccion = d
    def setTelefono(self, t): self.__telefono = t

    def __str__(self):
        return f"[Cliente] {super().__str__()} | Dir: {self.__direccion} | Tel: {self.__telefono}"