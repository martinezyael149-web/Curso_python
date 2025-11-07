

'''
Verificación de año bisiesto y edad legal:
Pide el año de nacimiento y determina si es bisiesto. Luego calcula la edad del usuario
y verifica si es mayor de edad (18+).
'''


def año_bisiesto():
    año = int(input("Ingrese su año de nacimiento: "))
    
    # Verificar si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")
    
    # Calcular la edad
    año_actual = 2024
    edad = año_actual - año
    
    # Verificar si es mayor de edad
    if edad >= 18:
        print(f"Tienes {edad} años. Eres mayor de edad.")
    else:
        print(f"Tienes {edad} años. No eres mayor de edad.")