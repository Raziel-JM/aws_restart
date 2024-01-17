"""
import random #Biblioteca para utilizar numeros aleatorios

print("\t\tBienvenidos a nuestro juego de adivina el número")
print("\nLa regla es simple: pensaré un número y tú lo adivinas")

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = int(input("Adivina uu numero entre 1 y 10: "))
    #si el numero que ingresa es igual al que tengo
    if guess == number:
        print(f"Adivinaste! El numero es {guess}")
        isGuessright = True
    else:
        print("Intenta de nuevo")
"""
import random

print("\t\tBienvenidos a nuestro juego de adivina el número")
print("\nLa regla es simple: pensaré en un número y tú tratarás de adivinarlo")

number = random.randint(1, 10)

isGuessRight = False

while not isGuessRight:
    guess = int(input("Adivina un número entre 1 y 10: "))
    
    if 1 <= guess <= 10:
        if guess == number:
            print(f"Adivinaste! El número es {guess}")
            isGuessRight = True
        else:
            if abs(guess - number) <= 2:
                print("Caliente. ¡Estás cerca!")
            else:
                print("Frío. Estás lejos.")
    else:
        print("Número fuera del rango. Debes ingresar un número entre 1 y 10. Intenta de nuevo.")
        
        
    
    """
    i = 1

while i <= 10:
    print(i)
    i+=1
    # i = i + 1
    
print("El número final es", i)
    

i = 0
final = 10
salto = 2

while i < final:
    print(x)
    i += 2
    """
