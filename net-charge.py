"""
Descripción del Código:
Este código realiza un cálculo de carga neta para una secuencia de insulina humana en función del pH. Utiliza información sobre los pKa de aminoácidos específicos y la composición de la secuencia de insulina para determinar la carga neta en diferentes valores de pH.

Nota: Este código utiliza Python 3.6 y tiene codificación utf-8.
"""

# Secuencia completa de preproinsulina humana
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Almacenar las partes restantes de la secuencia de insulina en variables
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

# pKa de aminoácidos específicos
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Conteo de aminoácidos en la secuencia de insulina
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Inicializar la variable de pH
pH = 0

# Bucle while para calcular la carga neta en diferentes valores de pH
while pH <= 14:
    # Calcular la carga neta
    netCharge = (
        +(sum({x: ((seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x])))
               for x in ['k', 'h', 'r']}.values()))
        -(sum({x: ((seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x])))
               for x in ['y', 'c', 'd', 'e']}.values())))
    
    # Imprimir la carga neta con el valor de pH
    print('{0:.2f}'.format(pH), netCharge)
    
    # Incrementar la variable de pH
    pH += 1

