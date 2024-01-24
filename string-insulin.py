"""
Este script de Python presenta una secuencia de operaciones relacionadas con la manipulación y el análisis de cadenas y el cálculo de pesos moleculares.

1. Se define la secuencia de aminoácidos 'preproInsulin' y se almacenan segmentos específicos en variables adicionales.
2. Se imprime la secuencia de preproinsulina en la consola utilizando la función `print()`.
3. Se crea un diccionario 'aaWeights' que contiene los pesos moleculares de los aminoácidos.
4. Se cuenta la frecuencia de cada aminoácido en la secuencia 'insulin' y se almacena en el diccionario 'aaCountInsulin'.
5. Se calcula el peso molecular aproximado de la insulina multiplicando la frecuencia de cada aminoácido por su peso y sumando los resultados.
6. Se imprime el peso molecular aproximado de la insulina.
7. Se compara el peso molecular aproximado con el peso molecular actual de la insulina y se imprime el porcentaje de error.
"""
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:

sInsulin = "malwmrllpllallalwgpdpaaa"

bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"

aInsulin = "giveqcctsicslyqlenycn"

cInsulin ="rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:

print("The sequence of human preproinsulin:")

print(preproInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
print('Conteo:',aaCountInsulin)

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
