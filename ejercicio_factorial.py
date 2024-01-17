"""
Your module description
"""
# Solicitar al usuario un número entero no negativo
n = int(input("Ingrese un número entero no negativo: "))
# Comprobar si el número es negativo
if n < 0:
    print("Error: el número debe ser no negativo.")
else:
    # Calcular el factorial usando un bucle 'for'
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    # Mostrar el resultado
    print("El factorial de", n, "es", factorial)