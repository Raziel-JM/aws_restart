"""
Descripción del Código:
Este código ilustra el uso del módulo `json` en Python para la serialización y deserialización de datos. Se presentan ejemplos de la conversión entre objetos Python y cadenas JSON, así como la escritura y lectura de datos JSON desde un archivo.
"""

import json

# Un objeto de ejemplo (diccionario en Python)
data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Ejemplo de json.dumps - convierte un objeto Python a una cadena JSON
json_string = json.dumps(data)
print("JSON string:", json_string, type(json_string))  # Muestra la cadena JSON y su tipo (str)

# Ejemplo de json.loads - convierte una cadena JSON a un objeto Python
python_obj = json.loads(json_string)
print("Python object:", python_obj, type(python_obj))  # Muestra el objeto Python y su tipo (dict)

# Ejemplo de json.dump - escribe un objeto Python en un archivo JSON
with open('data.json', 'w') as file:
    json.dump(data, file)

# Ejemplo de json.load - lee un archivo JSON y lo convierte a un objeto Python
with open('data.json', 'r') as file:
    data_from_file = json.load(file)
    print("Data read from file:", data_from_file)  # Muestra los datos leídos del archivo
