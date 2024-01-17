"""
Your module description
"""
# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))
# Comprobar si el número es negativo
if n < 0:
    print("Error: el número debe ser positivo.")
else:
    # Contar los números pares e impares
    pares = 0
    impares = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    # Mostrar los resultados
    print("Números pares:", pares)
    print("Números impares:", impares)