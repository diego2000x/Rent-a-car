from conex.conn import Conex
import traceback

class DaoSucursal:
    def __init__(self):
        self.database = "viaja_seguro_rentacar"

    def registrarSucursal(self, sucursal):
        conn = Conex("localhost", "root", "", self.database)
        sql = "INSERT INTO Sucursal (direccion, fono, correo) VALUES (%s, %s, %s)"
        msg = ""
        try:
            c = conn.getConex().cursor()
            # El código es autoincremental en BD, no se envía
            c.execute(sql, (sucursal.getDireccion(), sucursal.getFono(), sucursal.getCorreo()))
            conn.getConex().commit()
            msg = "Sucursal registrada correctamente."
        except Exception as ex:
            print(traceback.print_exc())
            msg = "Error al registrar sucursal."
        finally:
            conn.closeConex()
        return msg

    def listarEmpleadosSucursal(self, codigo_sucursal):
        # Query para obtener solo empleados de esa sucursal
        conn = Conex("localhost", "root", "", self.database)
        sql = "SELECT run, nombre, apellido, codigo, cargo, password, sucursal_codigo FROM Empleado WHERE sucursal_codigo = %s"
        datos = []
        try:
            c = conn.getConex().cursor()
            c.execute(sql, (codigo_sucursal,))
            datos = c.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            conn.closeConex()
        return datos

    def listarVehiculosSucursal(self, codigo_sucursal):
        # Query para obtener solo vehículos de esa sucursal
        conn = Conex("localhost", "root", "", self.database)
        sql = "SELECT patente, marca, modelo, anio, precio, disponible FROM Vehiculo WHERE sucursal_codigo = %s"
        datos = []
        try:
            c = conn.getConex().cursor()
            c.execute(sql, (codigo_sucursal,))
            datos = c.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            conn.closeConex()
        return datos