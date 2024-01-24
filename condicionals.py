"""
Este módulo presenta un pequeño programa de interacción con el usuario en el contexto de un servicio de entrega y una tienda de artículos de oficina. El código utiliza la entrada del usuario para determinar si necesita ayuda con la entrega de un paquete y, en caso afirmativo, ofrece asistencia. Luego, pregunta al usuario si desea comprar estampas, una caja o hacer copias, y responde en consecuencia. La importancia de este código radica en su capacidad para manejar respuestas del usuario y proporcionar información relevante basada en esas respuestas.
"""

# Pregunta al usuario si necesita ayuda con la entrega de un paquete
userReply = input("Necesitas que te entreguemos un paquete? (si o no)")

# Verifica la respuesta del usuario y proporciona una respuesta apropiada
if userReply == "si":
    print("Podemos ayudarte a entregar tu paquete")
else:
    print("Gracias, vuelva pronto")

# Pregunta al usuario qué artículo desea comprar: estampas, una caja o hacer copias
userReply = input("Quisiers comprar estampas, una caja o copia? ")

# Verifica la respuesta del usuario y proporciona respuestas específicas
if userReply == "estampas":
    print("Tenemos diferentes estampas para ti")
elif userReply == "caja":
    print("Tenemos diferentes tamaños de cajas")
elif userReply == "copia":
    # Solicita al usuario la cantidad de copias que desea hacer
    copies = input("Cuántas copias quieres sacar?")
    print(f"Aquí hay {copies} copias")
else:
    print("Opción no válida")
