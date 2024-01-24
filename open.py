"""
Descripción del Código:
Este código ejemplifica la lectura de un archivo de texto y muestra su contenido. También se presenta un formato JSON de ejemplo.

Temas Cubiertos:
- Apertura y lectura de un archivo de texto en modo lectura y escritura (`rw+b`).
- Lectura del contenido completo del archivo con el método `read`.
"""

### Contador de palabras
## como ejemplo una canción

# Apertura del archivo en modo lectura y escritura
with open("enunciados.txt", mode="r+") as file:
    # Lee el contenido completo del archivo
    text = file.read()
    print(text)

# Formato JSON de ejemplo
formato_json = '{"clave":valor}'
