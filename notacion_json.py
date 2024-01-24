"""
Descripción del Código:
Este código demuestra el uso de la biblioteca `json` en Python para trabajar con objetos JSON. Se ejemplifican las funciones `json.dumps`, `json.loads`, `json.dump` y `json.load`.

Temas Cubiertos:
- Conversión de objeto Python a cadena JSON (`json.dumps`).
- Conversión de cadena JSON a objeto Python (`json.loads`).
- Escritura de objeto Python en un archivo JSON (`json.dump`).
- Lectura de un archivo JSON y conversión a objeto Python (`json.load`).
- Uso básico de la biblioteca `json`.

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
print("JSON string:", json_string)

"""
# Ejemplo de json.loads - convierte una cadena JSON a un objeto Python
python_obj = json.loads(json_string)
print("Python object:", python_obj)

# Ejemplo de json.dump - escribe un objeto Python en un archivo JSON
with open('data.json', 'w') as file:
    json.dump(data, file)

# Ejemplo de json.load - lee un archivo JSON y lo convierte a un objeto Python
with open('data.json', 'r') as file:
    data_from_file = json.load(file)
    print("Data read from file:", data_from_file)
"""

conteo = [{"a": 2}, {"b": 45}]

for dic in conteo:
    print(dic)
