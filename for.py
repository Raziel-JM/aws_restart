"""
Descripción del Código:
Este código realiza un conteo hasta 10 utilizando diferentes formas de la función `range()` en Python. Se utiliza un bucle for para iterar sobre los valores generados por `range()` y se muestra el conteo en cada caso.
"""

print("Conteo hasta 10")

# Utilizando rango
inicio = 0
final = 10

# Range con dos argumentos
print("\nRange con dos argumentos")

# range(inicio, final hasta (no lo toma)) con aumento de 1
for x in range(inicio, final + 1):
    print(x)

# Range con un argumento
print("\nRange con un argumento")

# range(final) con aumento de 1 y da por hecho que inicia en 0
for x in range(final + 1):
    print(x)

# Range con tres argumentos
print("\nRange con tres argumentos")

# range(inicio, final, salto)
salto = 2

for x in range(inicio, final + 1, salto):
    print(x)
