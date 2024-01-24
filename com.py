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

# Inicializar una lista vacía para almacenar diccionarios de vehículos (inventario)
myInventoryList = []

# Administrar el archivo CSV llamado 'car-fleet.csv'
with open('car-fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  # Configurar lector CSV
    lineCount = 0  # Inicializar contador de líneas

    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            # Imprimir detalles de cada vehículo leído desde el archivo CSV
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')

            # Crear una copia profunda del diccionario myVehicle y asignar valores desde el archivo CSV
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            # Agregar el diccionario del vehículo a la lista de inventario
            myInventoryList.append(currentVehicle)
            lineCount += 1

    print(f'Processed {lineCount} lines.')

# Imprimir detalles de cada vehículo en la lista de inventario
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
        print("-----")
    print()
