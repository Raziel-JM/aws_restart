"""
Este script de Python muestra el uso de aserciones para verificar condiciones específicas durante la ejecución del programa. En el ejemplo, se utiliza el módulo 'os' para limpiar la pantalla, y se definen funciones que incluyen aserciones para validar ciertas condiciones.

1. Se utiliza 'os.system("clear")' para limpiar la pantalla (asume que se está ejecutando en un sistema Unix-like).

2. La función 'dividir' realiza la división de dos números y utiliza una aserción para asegurarse de que el divisor no sea cero.

3. Se llama a la función 'dividir' con un divisor igual a cero, activando la aserción y mostrando un mensaje de error.

4. La función 'loguser' toma la edad como argumento y utiliza una aserción para verificar que la edad sea mayor que 0.

5. Se llama a la función 'loguser' con un argumento no válido ("hola"), activando la aserción y mostrando un mensaje de error.

Las aserciones son útiles para atrapar errores y condiciones inesperadas durante el desarrollo del programa, facilitando la detección y corrección de problemas.
"""
import os

# Limpiar la pantalla (se asume que se está ejecutando en un sistema Unix-like)
os.system("clear")

a = 5

def dividir(a, b):
    # Aserción para verificar que b no sea 0
    assert b != 0, "El divisor no puede ser cero"
    return a / b

# La aserción se activará si b es 0
resultado = dividir(0, 5)
#print(resultado)

def loguser(age):
    # Aserción para verificar que la edad sea mayor que 0
    assert age > 0, "Edad no válida"

# La aserción se activará si age no es un número válido
loguser("hola")
