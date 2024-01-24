"""
Ejercicio 3: Calculadora de Números Primos

Descripción: 
Escribe una función que tome un número entero y devuelva True si el número es primo y False en caso contrario. 
Luego, utiliza esta función en un programa que pida al usuario ingresar un número y muestre en pantalla si es primo o no.

Consejos: Recuerda que un número primo es un número mayor que 1 que solo tiene dos divisores: 1 y él mismo.
"""
print("Ejercicio 3: Calculadora de Números Primos")
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar al usuario un número entero
try:
    numero_usuario = int(input("\nIngrese un número entero: "))
    if numero_usuario < 0:
        print("\nError: Por Favor Ingrese un número entero no negativo!!.")
    else:
        # Verificar si el número es primo y mostrar el resultado
        if primo(numero_usuario):
            print(f"\nEl número {numero_usuario} si es un número primo. :)")
        else:
            print(f"\nEl número {numero_usuario} no es un número primo. :(")
except ValueError:
    print("\nError: Ingrese un número entero válido.")
