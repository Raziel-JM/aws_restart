"""
Descripción del Código:
Este código presenta ejemplos de variables, listas, tuplas y operaciones en Python. Incluye ejemplos de asignación de variables, manipulación de listas, bucles for y la diferencia entre listas y tuplas.
"""

# Ejemplo de lista y tupla con las variables definidas anteriormente
# Se utiliza el mismo nombre, director y fecha para ambos ejemplos

# Definición de variables
nombre = "Titanic"
director = "James Cameron"
fecha = 1997

# Ejemplo de comentario simple y comentario con print comentado
# print("Hola como estas esto es un argumento")

# Definición de variables para el ejemplo de frutas
fruta1 = "Manzana"
fruta2 = "Pera"

# Ejemplo de comentario con print comentado utilizando f-strings
# print(f"La fruta1 es {fruta1} y la 2 es {fruta2}")

# Asignación de valor de fruta2 a fruta1
fruta1 = fruta2

# Ejemplo de comentario con print comentado utilizando f-strings después de la asignación
# print(f"La fruta1 es {fruta1} y la 2 es {fruta2}")

# Lista mixta de tipos de datos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Lista de números y bucle for para duplicar cada número y almacenar en una nueva lista
numeros = [45, 23, 10]
total = []

for x in numeros:
    temp = x * 2
    total.append(temp)

# Imprimir la nueva lista con números duplicados
print("Lista de números duplicados:", total)

# Ejemplo de tupla con las variables de nombre, director y fecha
# La tupla es inmutable y se define utilizando paréntesis ()
miTupla = (nombre, director, fecha)

# Imprimir la tupla
print("Tupla de información:", miTupla)
