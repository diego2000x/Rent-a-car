from modelo.persona import Persona

class Empleado(Persona):
    def __init__(self, run="", nombre="", apellido="", codigo=0, cargo="", password="", sucursal_codigo=None):
        super().__init__(run, nombre, apellido) # Herencia
        self.__codigo = codigo
        self.__cargo = cargo
        self.__password = password
        self.__sucursal_codigo = sucursal_codigo

    def getCodigo(self): return self.__codigo
    def getCargo(self): return self.__cargo
    def getPassword(self): return self.__password
    def getSucursalCodigo(self): return self.__sucursal_codigo

    def __str__(self):
        return f"[Empleado] Código: {self.__codigo} | {super().__str__()} | Cargo: {self.__cargo}"