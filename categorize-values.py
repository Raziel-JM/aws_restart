# Define una lista con diferentes tipos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Utiliza un bucle for para recorrer la lista e imprimir el tipo de dato de cada elemento
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))
