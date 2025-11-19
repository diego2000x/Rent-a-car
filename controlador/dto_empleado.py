from modelo.empleado import Empleado
from controlador.dao_empleado import DaoEmpleado
from utils.encoder import Encoder

class EmpleadoDTO:
    
    def validarLogin(self, run, password_plana):
        dao = DaoEmpleado()
        resultado = dao.validarLogin(run)
        
        # resultado trae la tupla de la BD. resultado[5] es el hash de la password.
        if resultado is not None:
            pass_hash_bd = resultado[5]
            if Encoder().decode(password_plana, pass_hash_bd):
                # Login Exitoso: Retornamos objeto Empleado
                return Empleado(resultado[1], resultado[2], resultado[3], resultado[0], resultado[4], resultado[5], resultado[6])
        return None

    def agregarEmpleado(self, run, nombre, apellido, cargo, password, sucursal_id):
        # Encriptamos la password antes de enviarla al DAO
        pass_encrypted = Encoder().encode(password)
        empleado = Empleado(run, nombre, apellido, 0, cargo, pass_encrypted, sucursal_id)
        dao = DaoEmpleado()
        return dao.agregarEmpleado(empleado)

    def listarEmpleados(self):
        dao = DaoEmpleado()
        datos = dao.listarEmpleados()
        lista_empleados = []
        if datos:
            for row in datos:
                # Creamos objetos Empleado por cada fila
                emp = Empleado(row[1], row[2], row[3], row[0], row[4], row[5], row[6])
                lista_empleados.append(emp)
        return lista_empleados