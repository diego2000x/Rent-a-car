from modelo.sucursal import Sucursal
from modelo.empleado import Empleado
from modelo.vehiculo import Vehiculo
from controlador.dao_sucursal import DaoSucursal

class SucursalDTO:
    
    def registrarSucursal(self, direccion, fono, correo):
        # Creamos el objeto sucursal
        sucursal = Sucursal(0, direccion, fono, correo)
        dao = DaoSucursal()
        return dao.registrarSucursal(sucursal)

    def listarEmpleadosPorSucursal(self, codigo_sucursal):
        dao = DaoSucursal()
        datos = dao.listarEmpleadosSucursal(codigo_sucursal)
        lista_empleados_obj = []
        
        # Convertir tuplas a objetos Empleado
        if datos:
            for row in datos:
                # row: (run, nombre, apellido, codigo, cargo, password, sucursal_codigo)
                emp = Empleado(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                lista_empleados_obj.append(emp)
        
        return lista_empleados_obj

    def listarVehiculosPorSucursal(self, codigo_sucursal):
        dao = DaoSucursal()
        datos = dao.listarVehiculosSucursal(codigo_sucursal)
        lista_vehiculos_obj = []
        
        # Convertir tuplas a objetos Vehiculo
        if datos:
            for row in datos:
                # row: (patente, marca, modelo, anio, precio, disponible)
                veh = Vehiculo(row[0], row[1], row[2], row[3], float(row[4]), row[5])
                lista_vehiculos_obj.append(veh)
                
        return lista_vehiculos_obj