"""
Ejercicio 7: Contador de Palabras
Descripción:
Este programa en Python cuenta el número de veces que cada palabra aparece en una cadena de texto dada por el usuario.
Ignora las diferencias entre mayúsculas y minúsculas y excluye los signos de puntuación.
"""
import string

def contar_palabras(cadena):
    """
    Cuenta el número de veces que cada palabra aparece en una cadena de texto.

    Args:
        cadena (str): La cadena de texto a analizar.

    Returns:
        dict: Un diccionario donde las claves son las palabras y los valores son sus conteos.
    """
    # Eliminar signos de puntuación y convertir todo a minúsculas
    translator = str.maketrans("", "", string.punctuation)
    cadena = cadena.translate(translator).lower()

    # Dividir la cadena en palabras y contar usando dict comprehension
    conteo_palabras = {word: cadena.split().count(word) for word in set(cadena.split())}

    return conteo_palabras

def main():
    """
    Función principal que maneja la ejecución del programa.
    """
    print("Contador de Palabras")

    # Solicitar la cadena de texto al usuario
    cadena = input("\nIngrese una cadena de texto: ")

    # Obtener el conteo de palabras
    resultado = contar_palabras(cadena)

    # Mostrar el resultado
    print("\nConteo de palabras:")
    for palabra, conteo in resultado.items():
        print(f"{palabra}: {conteo}")

if __name__ == "__main__":
    main()