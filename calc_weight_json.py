import jsonFileHandler

# Recupere los datos JSON y almacénelos en una variable de datos.
data = jsonFileHandler.readJsonFile('files/insulin.json')

# Compruebe si los datos devueltos no están vacíos y obtenga los datos de insulina.
if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

    # Calculando el peso molecular de la insulina
    # Obtener una lista de los pesos de los aminoácidos (AA)
    aaWeights = data['weights']
    # Contar el número de cada aminoácido
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']}
    # Multiplicar el recuento por los pesos
    molecularWeightInsulin = sum({x: (aaCountInsulin[x] * aaWeights[x]) for x in
                                  ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))

else:
    print("Error. Exiting program")
