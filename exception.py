"""
Descripción del Código:
Este código ejemplifica el manejo de excepciones en Python al realizar una operación de división. Se utiliza un bloque try-except para manejar posibles errores, como la división por cero o el ingreso de datos no numéricos.
"""

try:
    # Solicita al usuario ingresar dos números
    a = int(input("Ingresa un número: "))
    b = int(input("Ingresa otro número: "))
    
    # Intenta realizar la división y muestra el resultado
    total = a / b
    print("El resultado de la división es", total)

# Manejo de excepciones para ZeroDivisionError
except ZeroDivisionError:
    print("No se puede dividir entre 0")

# Manejo de excepciones para ValueError (ingreso de datos no numéricos)
except ValueError:
    print("Ingresaste algo que NO es un número")

# Este bloque se ejecuta siempre, independientemente de si hay excepciones o no
print("Mensaje importante")
