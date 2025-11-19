from conex.conn import Conex
import traceback

class DaoArriendo:
    def __init__(self):
        self.database = "viaja_seguro_rentacar"

    def buscar_vehiculo_por_patente(self, patente):
        # Método auxiliar para traer datos del auto (sobre todo precio UF)
        conn = Conex("localhost", "root", "", self.database)
        sql = "SELECT patente, marca, modelo, anio, precio, disponible FROM Vehiculo WHERE patente = %s"
        res = None
        try:
            c = conn.getConex().cursor()
            c.execute(sql, (patente,))
            res = c.fetchone()
        except Exception:
            traceback.print_exc()
        finally:
            conn.closeConex()
        return res

    def registrarArriendo(self, arriendo):
        conn = Conex("localhost", "root", "", self.database)
        # Transacción: Insertar Arriendo Y actualizar Vehículo a 'N'
        sql_arriendo = """
            INSERT INTO Arriendo (fechaInicio, fechaEntrega, costoTotal, cliente_run, empleado_codigo, vehiculo_patente) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        sql_update_vehiculo = "UPDATE Vehiculo SET disponible = 'N' WHERE patente = %s"
        
        msg = ""
        try:
            c = conn.getConex().cursor()
            # 1. Insertar Arriendo
            c.execute(sql_arriendo, (
                arriendo.getFechaInicio(),
                arriendo.getFechaEntrega(),
                arriendo.getCostoTotal(),
                arriendo.getClienteRun(),
                arriendo.getEmpleadoCodigo(),
                arriendo.getVehiculoPatente()
            ))
            
            # 2. Bloquear Vehículo
            c.execute(sql_update_vehiculo, (arriendo.getVehiculoPatente(),))
            
            conn.getConex().commit()
            msg = f"Arriendo generado con éxito. Total a pagar: ${arriendo.getCostoTotal()}"
        except Exception as ex:
            conn.getConex().rollback() # Si falla algo, deshace todo
            msg = f"Error en la transacción: {ex}"
            print(traceback.print_exc())
        finally:
            conn.closeConex()
        return msg