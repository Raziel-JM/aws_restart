"""
Ejercicio 2: Contador de números pares e impares
Este código solicita al usuario un número entero positivo. Luego, verifica si el número ingresado es negativo. 
Si es negativo, muestra un mensaje de error. Si es positivo, cuenta los números pares e impares hasta el número ingresado y muestra los resultados.
"""
print("Ejercicio 2: Contador de números pares e impares")
# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))
# Comprobar si el número es negativo
if n < 0:
    print("\nError: El número debe ser positivo.")
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
    print("\nNúmeros pares:", pares)
    print("\nNúmeros impares:", impares)
