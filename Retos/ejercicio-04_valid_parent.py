"""
Ejercicio 4: Validador de Paréntesis

Descripción:
Escribe una función que tome una cadena de caracteres que contiene solo paréntesis ( y ) y determine si la secuencia de paréntesis es válida. 
Una secuencia de paréntesis es válida si cada paréntesis abierto se cierra con un paréntesis correspondiente en el orden correcto. 
Por ejemplo, "(())()" y "()" son secuencias válidas, pero ")(" y "(()" no lo son.

Consejos:
Puedes usar una pila para realizar un seguimiento de los paréntesis. 
Cada vez que encuentres un paréntesis abierto, empújalo a la pila. 
Cuando encuentres un paréntesis cerrado, comprueba si se corresponde con el último paréntesis abierto (pop de la pila).
"""
# Imprimir información sobre el ejercicio
print("Ejercicio 4: Validador de Paréntesis")

def valida(secuencia ):
    """
    Función que valida si una secuencia de paréntesis es correcta.
    
    Parámetros:
    secuencia (str): La secuencia de paréntesis.
    
    Retorna:
    bool: True si la secuencia es válida, False en caso contrario.
    """
    pila = []  # Inicializar una pila vacía para realizar un seguimiento de los paréntesis
    for char in secuencia:
        if char == '(':
            pila.append(char)  # Empujar paréntesis abierto a la pila
        elif char == ')':
            # Verificar si hay un paréntesis abierto correspondiente en la pila
            if len(pila) == 0 or pila[-1] != '(':
                return False
            pila.pop()  # Pop el paréntesis abierto correspondiente
    return len(pila) == 0  # La secuencia es válida si la pila está vacía al final

# Solicitar al usuario una secuencia de paréntesis
secuencia = input("\nIngrese una secuencia de paréntesis: ")

# Verificar si la secuencia de paréntesis es válida y mostrar el resultado
if valida(secuencia):
    print("\nLa secuencia de paréntesis es válida.")
else:
    print("\nLa secuencia de paréntesis no es válida.")
