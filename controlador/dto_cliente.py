from modelo.cliente import Cliente
from controlador.dao_cliente import DaoCliente

class ClienteDTO:
    def agregarCliente(self, run, nombre, apellido, direccion, telefono):
        # Aquí podrías agregar validaciones extra (ej: largo del run)
        cliente = Cliente(run, nombre, apellido, direccion, telefono)
        dao = DaoCliente()
        return dao.agregarCliente(cliente)

    def listarClientes(self):
        dao = DaoCliente()
        datos = dao.listarClientes()
        lista_objetos = []
        for row in datos:
            # Convertimos las tuplas de la BD en Objetos Cliente
            cli = Cliente(row[0], row[1], row[2], row[3], row[4])
            lista_objetos.append(cli)
        return lista_objetos