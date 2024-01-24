"""
Este código muestra cómo manipular cadenas de texto en Python. Comienza dividiendo un texto en una lista de palabras utilizando la coma como delimitador, luego une las palabras en un nuevo texto usando la coma como separador. Además, asegura que los elementos en una lista de frutas sean de tipo string antes de unirlos en un nuevo texto usando el asterisco como separador. Finalmente, imprime los textos resultantes y sus tipos de datos.
"""

text = "Hola como estas, muy bien espero"

# Separar el texto en una lista usando la coma como delimitador
palabras = text.split(",") 

# Unir la lista de palabras en un nuevo texto usando la coma como separador
nuevotxt = ",".join(palabras)

# Imprimir el nuevo texto y su tipo de dato
#print(nuevotxt, type(nuevotxt))

frutas = ["Manzana", "Pera", "Uva", 4]

# Convertir elementos que no son strings en la lista de frutas a strings
for i in range(len(frutas)):
    if type(frutas[i]) != str:
        frutas[i] = str(frutas[i])

# Unir la lista de frutas en un nuevo texto usando el asterisco como separador
txt = "*".join(frutas)

# Imprimir el texto resultante
print("Las frutas son", txt)
