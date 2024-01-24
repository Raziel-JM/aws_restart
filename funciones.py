"""
Descripción del Código:
Este código muestra ejemplos de funciones en Python, incluyendo definición de funciones, parámetros, retorno de valores, y el uso de la palabra clave 'pass' para suplir temporalmente la ausencia de contenido en una función.
"""

# Variables y operación de suma
a = 5
b = 4
total = a + b

# Funciones
## Definición de función sumar
def sumar(a, b):
    total = a + b
    return total # 'return' nos ayuda a devolver un valor

## Llamadas a la función sumar con diferentes argumentos
total1 = sumar(a=5, b=6)
total2 = sumar(a=3, b=4)

#print("El retorno de la función es", total1, "y", total2)

## Función operacionDificil con la palabra clave 'pass'
def operacionDificil(radio, pi, altura, diametro, ancho):
    pass # Suplir por un momento la ausencia de contenido en una función

## Llamada a la función operacionDificil con argumentos
operacionDificil(radio=5, pi=4, altura=3, diametro=10, ancho=2)

## Función suma con impresión y retorno
def suma(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")
    return resultado

## Llamada a la función suma
resultado = suma(3, 5)

#print(resultado)

## Definición de función demo con un parámetro k
a, b, c = 1, 2, 3
def demo(k):
    y = a + b + c
    return y

## Llamada a la función demo con argumento 7
print(demo(7))

## Uso de la función help con la función round
nombre = "Raziel"
print(help(round))

    
