"""
Ejercicio 6: Convertidor de Temperatura
Descripción:
Este programa en Python es un convertidor de temperaturas entre grados Celsius (°C) y Fahrenheit (°F). 
La conversión se realiza mediante dos funciones: `convertir_temperatura` y `main`.
"""

def convertir_temperatura(temperatura, unidad_original):
    """
    Convierte la temperatura de una unidad dada (Celsius o Fahrenheit) a la otra.
    
    Args:
        temperatura (float): La temperatura a convertir.
        unidad_original (str): La unidad original ('C' para Celsius, 'F' para Fahrenheit).
    
    Returns:
        tuple or None: Una tupla con la temperatura convertida y la unidad convertida, o None si la unidad no es válida.
    """
    if unidad_original.lower() == 'c':
        # Convertir Celsius a Fahrenheit
        temperatura_convertida = (temperatura * 9/5) + 32
        unidad_convertida = 'Fahrenheit'
    elif unidad_original.lower() == 'f':
        # Convertir Fahrenheit a Celsius
        temperatura_convertida = (temperatura - 32) * 5/9
        unidad_convertida = 'Celsius'
    else:
        print("\nUnidad de temperatura no válida.")
        return None, None
    
    return temperatura_convertida, unidad_convertida

def main():
    
    #Función principal que maneja la ejecución del programa.
    print("Bienvenido al Convertidor de Temperatura")

    # Solicitar la conversión deseada
    unidad_original = input("\nIngrese la unidad de temperatura original (C para Celsius, F para Fahrenheit): ")

    # Solicitar la temperatura
    try:
        temperatura = float(input("\nIngrese la temperatura: "))
    except ValueError:
        print("\nIngrese una temperatura válida.")
        return

    # Realizar la conversión
    temperatura_convertida, unidad_convertida = convertir_temperatura(temperatura, unidad_original)

    # Mostrar el resultado
    if temperatura_convertida is not None:
        print(f"\nLa temperatura de {temperatura:.2f}° grados {unidad_original.upper()} es igual a {temperatura_convertida:.2f}° grados {unidad_convertida}.")

if __name__ == "__main__":
    main()
