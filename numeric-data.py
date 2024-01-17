"""
Your module description
"""
# Mensaje introductorio
print("Python tiene 3 tipos de datos numéricos: int, float y complex")

# Comentario explicando la razón por la que este mensaje no se imprime
# ya que está dentro de un bloque de triple comilla, que es utilizado
# para comentarios de varias líneas pero no se muestra en la salida.

"""
No puede comenzar con un número.
No puede contener espacios en blanco.
No puede contener caracteres especiales, excepto el guión bajo (_).
No puede ser una palabra reservada.
Sensible a mayúsculas y minúsculas.
No debe utilizar caracteres acentuados ni espacios.
No debe comenzar con guión doble (__).
Evitar usar nombres que sobrescriban funciones integradas.
No debe ser demasiado largo o confuso.
"""

# Declaración e impresión de variables con distintos tipos de datos
miVariable = 10
print(miVariable, type(miVariable))

miVariable = 5.7
print(miVariable, type(miVariable))

miVariable = 2 + 6j
print(miVariable, type(miVariable))

# Conversión de un número entero a flotante
numero = 5
numero_convertido = float(numero)
print(numero_convertido)

# Conversión de un string a un entero
variable = "5"
variable_convertida = int(variable)
print(variable_convertida)

# Conversión de un número a string
variable = 56
variable_convertida = str(variable)
print(variable_convertida, type(variable_convertida))

# Impresión de variables concatenadas
nombre = "Juan"
apellido = "Perez"
print("Hola mi nombre es " + nombre + " " + apellido)
# Sinónimo usando f-strings
print(f"Hola mi nombre es {nombre} {apellido}")

# Tipos booleanos (True/False)
llover = True
nublado = False
print(llover, type(llover))

# Operaciones booleanas: and, or, not
print("\nOperación booleanos:")
print(llover and nublado)

# Ejemplo de operación de residuo/módulo
a = 7
b = 2
print("\nOperación de residuo/módulo:")
print(a % b)
