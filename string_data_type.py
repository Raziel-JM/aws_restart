"""
Este script de Python muestra ejemplos de manipulación de cadenas y entrada de usuario.

1. Se utiliza una variable 'myString' para almacenar cadenas. Pueden usarse comillas simples o dobles.
2. Se proporciona una sección con ejemplos de secuencias de escape, como \" para comillas y \n para salto de línea.
3. Se muestra cómo concatenar (unir) cadenas usando el operador '+'. También se puede usar el operador '+='.
4. Se utiliza la función 'input()' para recibir datos del usuario. El resultado es una cadena.
5. Se convierte la entrada de usuario a números enteros usando 'int()' para realizar operaciones matemáticas.
6. Se utiliza la f-string y la función 'format()' para formatear e imprimir mensajes que incluyen variables.

"""
myString = "Esto es un string"  # abrir y cerrar con comillas
myString = 'Esto también es un string'

"""
\" para escribir comillas dobles o simples
\n salto de linea o enter
\t tab
"""

nombre = "Raziel"

nombre = nombre + " Jiménez"
# nombre += "Vejarano"

# Imprime el mensaje utilizando concatenación
# print("Hola, mucho gusto tu nombre es "+nombre+" bienvenido")

# La función 'input()' toma la entrada del usuario (siempre como cadena)
nombre = input("¿Cómo es tu nombre? ")

# Imprime el mensaje utilizando f-string y entrada del usuario
print(f"Hola {nombre}")

# La función 'input()' devuelve una cadena, convertirla a int para operaciones matemáticas
numero1 = input("Ingresa un número: ")
numero1 = int(numero1)

# Convierte la entrada de usuario directamente a int para operaciones matemáticas
numero2 = int(input("Ingresa otro número: "))

# Realiza una operación matemática y muestra el resultado utilizando format()
total = numero1 + numero2
# print(f"{nombre} el resultado de la suma es {total}")
print("{} el resultado de la suma es {}".format(nombre, total))
