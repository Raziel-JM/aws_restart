# Función para obtener un doble alfabeto
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Función para obtener un mensaje del usuario
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Función para obtener una clave de cifrado del usuario
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Ejemplo de uso de las funciones
alphabet = "ABC"
doubleAlphabet = getDoubleAlphabet(alphabet)
message = getMessage()
cipherKey = getCipherKey()

print("Doble alfabeto:", doubleAlphabet)
print("Mensaje a cifrar:", message)
print("Clave de cifrado:", cipherKey)
