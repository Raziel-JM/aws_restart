"""
Ejercicio 1: Calculadora de factorial
Este código solicita al usuario un número entero no negativo, verifica si es negativo y 
calcula el factorial del número utilizando un bucle 'for'. Finalmente, muestra el resultado del factorial.
"""
print("Ejercicio 1: Calculadora de factorial")

# Solicitar al usuario un número entero no negativo
n = int(input("\nIngrese un número entero no negativo: "))
# Comprobar si el número es negativo
if n < 0:
    print("\nError: El número debe ser no negativo.")
else:
    # Calcular el factorial usando un bucle 'for'
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    # Mostrar el resultado
    print("\nEl factorial de", n, "es", factorial)