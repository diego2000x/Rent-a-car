class Vehiculo:
    def __init__(self, patente, marca="", modelo="", anio=0, precio_uf=0.0, disponible="S"):
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__precio_uf = precio_uf
        self.__disponible = disponible

    def getPatente(self): return self.__patente
    def getPrecioUF(self): return self.__precio_uf
    def getDisponible(self): return self.__disponible
    
    def __str__(self):
        estado = "Disponible" if self.__disponible == "S" else "Arrendado"
        return f"{self.__patente} | {self.__marca} {self.__modelo} ({self.__anio}) | UF {self.__precio_uf} | {estado}"