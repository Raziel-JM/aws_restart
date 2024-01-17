"""
Your module description
"""
userReply = input("Necesitas que te entreguemos un paquete? (si o no)")

if userReply == "si":
    print("Podemos ayudarte a entregar tu paquete")
else :
    print("Gracias , vuelva pronto")

userReply = input("Quisiers comprar estampas, una caja o copia? ")

if userReply == "estampas":
    print("Tenemos diferentes estampas para ti")
elif userReply == "caja":
    print("Tenemos diferentes tamaños de cajas")
elif userReply == "copia":
    copies = input ("Cuántas copias quieres sacar?")
    print(f"Aqui hay {copies} copias")
else:
    print("Opcion no válida")