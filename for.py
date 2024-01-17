"""
Your module description
"""
print("Conteo hasta 10")

#utilizando rango
inicio = 0
final = 10

print("\nRange con dos argumentos")

# range(inicio, final hasta (no lo toma)) con aumento de 1
for x in range(inicio, final +1):
    print(x)

print("\n Range con un argumento")
# range(final) con aumento de 1 y da por hecho que inicia en 0
for x in range (final +1):
    print(x)

print("\n Range con tres argumentos")
# range(inicio, final, salto)
salto = 2

for x in range (inicio,final + 1,salto):
    print(x)