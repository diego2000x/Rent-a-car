class Sucursal:
    def __init__(self, codigo=0, direccion="", fono="", correo=""):
        self.__codigo = codigo
        self.__direccion = direccion
        self.__fono = fono
        self.__correo = correo
        # Listas vacías para cumplir con la relación de agregación (0..*)
        self.__empleados = [] 
        self.__vehiculos = []

    # Getters y Setters
    def getCodigo(self): return self.__codigo
    def getDireccion(self): return self.__direccion
    def getFono(self): return self.__fono
    def getCorreo(self): return self.__correo
    
    def setEmpleados(self, lista_empleados):
        self.__empleados = lista_empleados

    def setVehiculos(self, lista_vehiculos):
        self.__vehiculos = lista_vehiculos

    def __str__(self):
        return f"Sucursal #{self.__codigo} | {self.__direccion} | Contacto: {self.__fono}"