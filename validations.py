from controlador.dto_empleado import EmpleadoDTO
from controlador.dto_arriendo import ArriendoDTO
import getpass # Para ocultar la contraseña al escribir

# --- FUNCIONES DE AYUDA ---
def solicitar_datos_empleado():
    print("\n--- Registro de Nuevo Empleado ---")
    run = input("Run (12345678-9): ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo (Gerente/Vendedor): ")
    # getpass oculta lo que escribes (Requisito 2.1.12)
    pwd = getpass.getpass("Contraseña: ") 
    sucursal = input("Código Sucursal (ID numérico): ")
    return run, nombre, apellido, cargo, pwd, sucursal

# --- MENUS ---
def menu_principal():
    print("\n=== SISTEMA VIAJA SEGURO RENT A CAR ===")
    print("1. Gestión de Empleados (Solo Gerente)")
    print("2. Gestión de Clientes")
    print("3. Gestión de Arriendos")
    print("4. Salir")
    return input("Seleccione una opción: ")

def menu_empleados():
    print("\n--- GESTIÓN DE EMPLEADOS ---")
    print("1. Listar Empleados")
    print("2. Registrar Empleado")
    print("3. Volver")
    opc = input("Opción: ")
    
    if opc == '1':
        lista = EmpleadoDTO().listarEmpleados()
        for emp in lista:
            print(emp)
    elif opc == '2':
        datos = solicitar_datos_empleado()
        # Desempaquetamos los datos
        msg = EmpleadoDTO().agregarEmpleado(*datos)
        print(msg)

# --- LOGICA DE ARRANQUE ---
def inicial(empleado_logueado):
    while True:
        opc = menu_principal()
        
        if opc == '1':
            # VALIDACION DE ROL (Requisito: Solo Gerente)
            if empleado_logueado.getCargo().lower() == "gerente":
                menu_empleados()
            else:
                print("ACCESO DENEGADO: Solo Gerentes pueden gestionar empleados.")
                
        elif opc == '2':
            print("Funcionalidad Cliente en construcción...")
            # Aquí llamarías a menu_clientes()
            
        elif opc == '3':
            print("Funcionalidad Arriendo en construcción...")
            
        elif opc == '4':
            print("Cerrando sesión...")
            break

def login_sistema():
    print("\n|| LOGIN VIAJA SEGURO ||")
    run = input("Ingrese Run Usuario: ")
    pwd = getpass.getpass("Ingrese Contraseña: ") # Input seguro
    
    usuario = EmpleadoDTO().validarLogin(run, pwd)
    return usuario


def menu_arriendos(empleado_logueado):
    print("\n--- NUEVO ARRIENDO ---")
    patente = input("Patente del Vehículo: ")
    run_cliente = input("Run del Cliente: ")
    dias = input("Días de arriendo: ")
    
    # Usamos el código del empleado que inició sesión
    cod_empleado = empleado_logueado.getCodigo()
    
    dto = ArriendoDTO()
    mensaje = dto.generar_nuevo_arriendo(patente, run_cliente, cod_empleado, dias)
    print(mensaje)

from controlador.dto_sucursal import SucursalDTO

def prueba_sucursal():
    dto = SucursalDTO()
    
    # 1. Crear una nueva sucursal (ejemplo)
    print(dto.registrarSucursal("Av. Libertador 999", "22555666", "centro@viajaseguro.cl"))
    
    id_sucursal = 1 # Asumiendo que consultamos la sucursal 1
    
    # 2. Listar sus vehículos
    print(f"\n--- Vehículos en Sucursal {id_sucursal} ---")
    autos = dto.listarVehiculosPorSucursal(id_sucursal)
    for a in autos:
        print(a) # Usa el __str__ de Vehiculo
        
    # 3. Listar sus empleados
    print(f"\n--- Empleados en Sucursal {id_sucursal} ---")
    personal = dto.listarEmpleadosPorSucursal(id_sucursal)
    for p in personal:
        print(p) # Usa el __str__ de Empleado