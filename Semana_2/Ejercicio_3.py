'''
Validación de acceso:
Solicita usuario, contraseña y rol (admin, editor, visitante).
Verifica si las credenciales
son válidas y muestra los permisos disponibles según el rol. 
Usa múltiples condicionales
y lógica anidada.

'''

Usuarios={
    "admin_user": {"password": "admin123", "role": "admin"},
    "editor_user": {"password": "edit123", "role": "editor"},
    "visitor_user": {"password": "visit123", "role": "visitor"}
}

def validar_acceso():
    username= input("ingrese su usuario :")
    password= input("Ingrese su contaseña: ")
    # Validar credenciales
    if validar_credenciales(username, password):
        print("Acceso concedido")
        return True
    else:
        print("Acceso denegado")
        return False

def validar_credenciales(usuario, contraseña):
    # Aquí va tu lógica de validación
    # Por ejemplo, verificar contra una base de datos o archivo
    return True  # Cambiar por tu lógica real

if __name__ == "__main__":
    validar_acceso()
    
   
    