from conex.conn import Conex
import traceback

class DaoEmpleado:
    def __init__(self):
        try:
            self.__conn = Conex("localhost", "root", "", "viaja_seguro_rentacar")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.__conn

    def validarLogin(self, run):
        # Busca por RUN y recupera la contraseña hasheada y datos para crear el objeto
        sql = "SELECT codigo, run, nombre, apellido, cargo, password, sucursal_codigo FROM Empleado WHERE run = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (run,))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()
        return resultado

    def agregarEmpleado(self, empleado):
        sql = "INSERT INTO Empleado (run, nombre, apellido, cargo, password, sucursal_codigo) VALUES (%s, %s, %s, %s, %s, %s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (
                empleado.getRun(), 
                empleado.getNombre(), 
                empleado.getApellido(),
                empleado.getCargo(), 
                empleado.getPassword(),
                empleado.getSucursalCodigo()
            ))
            c.getConex().commit()
            if cursor.rowcount > 0:
                mensaje = "Empleado registrado satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Error al registrar empleado (¿Run repetido?)"
        finally:
            c.closeConex()
        return mensaje

    def listarEmpleados(self):
        sql = "SELECT codigo, run, nombre, apellido, cargo, password, sucursal_codigo FROM Empleado"
        c = self.getConex()
        result = []
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            c.closeConex()
        return result