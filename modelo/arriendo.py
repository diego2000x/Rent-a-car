from datetime import datetime

class Arriendo:
    def __init__(self, numArriendo=0, fechaInicio="", fechaEntrega="", cliente_obj=None, empleado_obj=None, vehiculo_obj=None, costoTotal=0):
        self.__numArriendo = numArriendo
        self.__fechaInicio = fechaInicio
        self.__fechaEntrega = fechaEntrega
        self.__cliente = cliente_obj
        self.__empleado = empleado_obj
        self.__vehiculo = vehiculo_obj
        self.__costoTotal = costoTotal

    # Getters necesarios para el DAO
    def getFechaInicio(self): return self.__fechaInicio
    def getFechaEntrega(self): return self.__fechaEntrega
    def getCostoTotal(self): return self.__costoTotal
    def getClienteRun(self): return self.__cliente.getRun()
    def getEmpleadoCodigo(self): return self.__empleado.getCodigo()
    def getVehiculoPatente(self): return self.__vehiculo.getPatente()

    def convertirAPeso(self, precio_uf_vehiculo, valor_uf_dia, dias_arriendo):
        """
        Lógica de negocio: Calcula el total en pesos.
        """
        total = precio_uf_vehiculo * valor_uf_dia * dias_arriendo
        self.__costoTotal = int(total)
        return self.__costoTotal

    def __str__(self):
        return f"Arriendo N°{self.__numArriendo} | Total: ${self.__costoTotal} | Auto: {self.__vehiculo.getPatente()}"