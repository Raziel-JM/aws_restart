# Módulo Laboratorio: Programa de Cifrado César Error #4
#
# En un laboratorio anterior, creaste un programa de cifrado César. Esta versión del
# programa tiene errores. Usa un depurador para encontrar el error y corregirlo.

# Duplicar el alfabeto dado
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Obtener un mensaje para encriptar
def getMessage():
    stringToEncrypt = input("Por favor, ingresa un mensaje para encriptar: ")
    return stringToEncrypt

# Obtener una clave de cifrado
def getCipherKey():
    shiftAmount = input("Por favor, ingresa una clave (número entero del 1 al 25): ")
    return shiftAmount

# Encriptar mensaje
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        # Se ha movido esta línea después de verificar si el carácter está en el alfabeto
        position = alphabet.find(currentCharacter)
        if currentCharacter in alphabet:
            newPosition = (position + int(cipherKey)) % 26
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter
    return encryptedMessage

# Desencriptar mensaje
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    # Se corrige para usar decryptKey en lugar de cipherKey
    return encryptMessage(message, decryptKey, alphabet)

# Lógica principal del programa
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alfabeto: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alfabeto Duplicado: {myAlphabet2}')
    myMessage = getMessage()
    print(f'Mensaje: {myMessage}')
    myCipherKey = getCipherKey()
    print(f'Clave de Cifrado: {myCipherKey}')
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Mensaje Encriptado: {myEncryptedMessage}')
    # Se corrige para mostrar el mensaje desencriptado
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Lógica principal
runCaesarCipherProgram()
