
import json

def readJsonFile(fileName):
    # Agregue una variable de datos como una cadena vacía
    data = ""

    # Abra el archivo JSON con la función open y analice el archivo con json.load
    with open(fileName) as json_file:
        # json.load lee el archivo JSON y devuelve el contenido como un diccionario de Python
        data = json.load(json_file)

    # Agregue un bloque try/except para hacer que esta función sea más confiable
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")

    # Retorno de la función
    return data
