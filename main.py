from validations import login_sistema, inicial

if __name__ == "__main__":
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        usuario_logueado = login_sistema()
        
        if usuario_logueado:
            print(f"\nBienvenido {usuario_logueado.getNombre()} {usuario_logueado.getApellido()} ({usuario_logueado.getCargo()})")
            inicial(usuario_logueado)
            break
        else:
            print("Credenciales incorrectas.")
            intentos += 1
            
    if intentos == max_intentos:
        print("Cuenta bloqueada por seguridad. Contacte al administrador.")