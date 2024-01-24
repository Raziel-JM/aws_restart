"""
Ejercicio 5: Juego del Ahorcado

Descripción:
Crea una versión simplificada del juego del ahorcado. El programa selecciona una palabra de una lista de palabras
y muestra guiones bajos (_) en lugar de cada letra. El usuario intenta adivinar las letras de la palabra.
Si el usuario adivina correctamente, se revela la letra en su posición correspondiente. El juego termina cuando el
usuario adivina toda la palabra o se agotan los intentos.

Consejos:
Usa listas para almacenar las letras de la palabra y los guiones bajos que se mostrarán al usuario.
Puedes utilizar un número fijo de intentos y disminuirlo cada vez que el usuario hace una conjetura incorrecta.
"""

import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "desarrollo", "ahorcado", "codigo"]
    return random.choice(palabras)

def inicializar_tablero(palabra):
    return ["_" for _ in palabra]

def imprimir_tablero(tablero):
    print(" ".join(tablero))

def imprimir_ahorcado(intentos):
    if intentos == 0:
        print("""
          -----------------------
          |                          
          |                          
          |                         
          |                        
          |                          
          |                         
          |                        
          |                   
        __|__
        """)
    elif intentos == 1:
        print("""
          -----------------------
          |                     |
          |                     |
          |                     O
          |                                       
          |                                       
          |                                       
          |                                      
          |                                    
        __|__
        """)
    elif intentos == 2:
        print("""
          -----------------------
          |                     |
          |                     |
          |                     O
          |                     |
          |                    
          |
          |                                      
          |                                    
        __|__
        """)
    elif intentos == 3:
        print("""
          -----------------------
          |                     |
          |                     |
          |                     O
          |                   \ |
          |                     |
          |                                      
          |                                    
        __|__
        """)
    elif intentos == 4:
        print("""
          -----------------------
          |                     |
          |                     |
          |                     O
          |                   \ | /
          |                     |
          |                                      
          |                                    
        __|__
        """)
    elif intentos == 5:
        print("""
          -----------------------
          |                     |
          |                     |
          |                     O
          |                   \ | /
          |                     |
          |                    /
          |                                    
        __|__
        """)
    else:
        print("""
          -----------------------                 
          |                     |                
          |                     |
          |                     O                  
          |                   \ | /    GAME
          |                     |      OVER
          |                    / \
          |                                    
        __|__
        """)

def adivinar_letra(palabra, tablero, letra):
    aciertos = 0
    for i in range(len(palabra)):
        if palabra[i] == letra:
            tablero[i] = letra
            aciertos += 1
    return aciertos

def main():
    print("¡Bienvenido al juego del Ahorcado!")
    print("\nAdivina la palabra secreta.")
    print("\nNOTA: Las letras deben ser ingresadas en minúsculas.")

    palabra_secreta = seleccionar_palabra()
    tablero = inicializar_tablero(palabra_secreta)
    intentos_maximos = 6
    intentos_realizados = 0

    while "_" in tablero and intentos_realizados < intentos_maximos:
        imprimir_tablero(tablero)
        imprimir_ahorcado(intentos_realizados)
        print(f"\nIntentos restantes: {intentos_maximos - intentos_realizados}")

        letra_usuario = input("Ingresa una letra: ")

        if letra_usuario.isalpha() and letra_usuario.islower() and len(letra_usuario) == 1:
            aciertos = adivinar_letra(palabra_secreta, tablero, letra_usuario)
            if aciertos == 0:
                print("Incorrecto. Pierdes un intento.")
                intentos_realizados += 1
            else:
                print(f"¡Correcto! Adivinaste {aciertos} letra(s).")
        else:
            print("Ingresa una letra minúscula válida.")

    imprimir_tablero(tablero)
    imprimir_ahorcado(intentos_realizados)

    if "_" not in tablero:
        print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
    else:
        print(f"¡Oh no! Te quedaste sin intentos. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    main()
