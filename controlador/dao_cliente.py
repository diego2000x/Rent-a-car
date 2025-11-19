from conex.conn import Conex
import traceback

class DaoCliente:
    def __init__(self):
        self.database = "viaja_seguro_rentacar" # Ajusta si tu DB se llama distinto

    def agregarCliente(self, cliente):
        conn = Conex("localhost", "root", "", self.database)
        sql = "INSERT INTO Cliente (run, nombre, apellido, direccion, telefono) VALUES (%s, %s, %s, %s, %s)"
        msg = ""
        try:
            c = conn.getConex().cursor()
            c.execute(sql, (cliente.getRun(), cliente.getNombre(), cliente.getApellido(), cliente.getDireccion(), cliente.getTelefono()))
            conn.getConex().commit()
            msg = "Cliente registrado correctamente."
        except Exception as ex:
            msg = "Error al registrar cliente (¿Run duplicado?)"
            print(traceback.print_exc())
        finally:
            conn.closeConex()
        return msg

    def listarClientes(self):
        conn = Conex("localhost", "root", "", self.database)
        sql = "SELECT run, nombre, apellido, direccion, telefono FROM Cliente"
        lista = []
        try:
            c = conn.getConex().cursor()
            c.execute(sql)
            lista = c.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            conn.closeConex()
        return lista