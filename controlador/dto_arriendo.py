from datetime import datetime
from modelo.arriendo import Arriendo
from modelo.vehiculo import Vehiculo
from modelo.cliente import Cliente
from modelo.empleado import Empleado
from controlador.dao_arriendo import DaoArriendo
from utils.mindicador import Mindicador # Tu archivo subido

class ArriendoDTO:
    
    def generar_nuevo_arriendo(self, patente, run_cliente, codigo_empleado, dias):
        dao = DaoArriendo()
        
        # 1. Validar datos del Vehículo
        datos_auto = dao.buscar_vehiculo_por_patente(patente)
        if not datos_auto:
            return "Error: Vehículo no existe."
        if datos_auto[5] == 'N': # Indice 5 es 'disponible'
            return "Error: El vehículo ya está arrendado."

        # Crear objeto vehículo temporal
        vehiculo = Vehiculo(datos_auto[0], datos_auto[1], datos_auto[2], datos_auto[3], float(datos_auto[4]))

        # 2. Consumir API para obtener UF
        api = Mindicador("uf")
        valor_uf = api.obtener_valor_actual()
        
        if valor_uf is None:
            # Fallback por si no hay internet: usar valor fijo o pedir manual (opcional)
            print("Advertencia: No se pudo conectar a la API. Usando valor referencia UF: 38000")
            valor_uf = 38000 

        # 3. Instanciar objetos auxiliares (Cliente y Empleado solo con ID para pasar al modelo)
        cliente = Cliente(run=run_cliente)
        empleado = Empleado(codigo=codigo_empleado)

        # 4. Calcular Fechas
        fecha_inicio = datetime.now().strftime("%Y-%m-%d")
        # (Lógica simple de fecha entrega para el ejemplo, idealmente sumar días reales)
        fecha_entrega = fecha_inicio 

        # 5. Crear Objeto Arriendo y Calcular Total
        arriendo = Arriendo(0, fecha_inicio, fecha_entrega, cliente, empleado, vehiculo)
        total_pesos = arriendo.convertirAPeso(vehiculo.getPrecioUF(), valor_uf, int(dias))

        # 6. Guardar en BD
        return dao.registrarArriendo(arriendo)