"""
Este módulo proporciona un ejemplo básico de manejo de archivos CSV en Python. El código utiliza el módulo 'csv' para leer un archivo llamado 'car-fleet.csv', que se espera contenga información sobre vehículos. Cada vehículo se representa como un diccionario con propiedades como 'vin', 'make', 'model', etc. El programa imprime las propiedades predeterminadas de un vehículo utilizando un diccionario llamado 'myVehicle'. La importación del módulo 'copy' se realiza para realizar copias profundas de diccionarios y evitar referencias no deseadas.
"""

import csv  # Importar módulo para manejar archivos CSV
import copy  # Importar módulo para realizar copias de elementos en Python

# Definir un diccionario para representar un vehículo con valores predeterminados
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Imprimir el contenido inicial del diccionario myVehicle
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))
