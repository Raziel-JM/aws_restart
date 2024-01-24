"""
Descripción del Código:
Este código define una función factorial iterativa y una función para calcular el área de un círculo. Luego, mide y compara el tiempo de ejecución entre la función factorial iterativa y la función factorial del módulo 'math'.

Adicionalmente, se utiliza la condición 'if __name__ == "__main__":' para ejecutar el código solo cuando el script es ejecutado directamente y no cuando es importado como un módulo.
"""

import time
import math

# Definición de la función factorial iterativo
def factorial_iterativo(n):
    if n == 0 or n == 1:
        # El factorial de 0 y 1 es 1
        return 1

    resultado = 1
    for i in range(2, n + 1):
        # Multiplica el resultado por cada número desde 2 hasta n
        resultado *= i
    
    return resultado

# Definición de la función para calcular el área de un círculo
def calcular_area(radio, pi=3.14):
    return pi * radio ** 2

# Bloque principal para medir tiempos
if __name__ == "__main__":
    # Número para calcular el factorial
    numero = 10
    
    # Medir el tiempo de la función factorial iterativa
    inicio = time.time()
    factorial_iterativo(numero)
    tiempo_recursivo = time.time() - inicio
    
    # Medir el tiempo de la función factorial del módulo math
    inicio = time.time()
    math.factorial(numero)
    tiempo_math = time.time() - inicio
    
    # Imprimir los tiempos de ejecución
    print("Tiempo función factorial iterativo:", tiempo_recursivo)
    print("Tiempo función factorial math:", tiempo_math)
