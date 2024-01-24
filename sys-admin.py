#import os

# Ejecutar el comando 'ls' utilizando os.system
#os.system("ls")

#import subprocess

# Ejecutar el comando 'ls' utilizando subprocess.run
#subprocess.run(["ls"])
#import subprocess

# Ejecutar el comando 'ls' con el argumento '-l' utilizando subprocess.run
#subprocess.run(["ls", "-l"])
#import subprocess

# Ejecutar el comando 'ls' con los argumentos '-l' y 'README.md' utilizando subprocess.run
#subprocess.run(["ls", "-l", "README.md"])

#import subprocess

# Definir el comando y sus argumentos
#command = "uname"
#commandArgument = "-a"

# Imprimir mensaje informativo
#print(f'Gathering system information with command: {command} {commandArgument}')

# Ejecutar el comando 'uname' con el argumento '-a'
#subprocess.run([command, commandArgument])
#import subprocess

# Definir el comando y sus argumentos
#command = "ps"

#commandArgument = "-x"

# Imprimir mensaje informativo
#print(f'Gathering active process information with command: {command} {commandArgument}')

# Ejecutar el comando 'ps' con el argumento '-x'
#subprocess.run([command, commandArgument])

# sys-admin.py

import subprocess

# Obtener información sobre el espacio en disco con el comando df
command = "df"
print(f'Gathering disk space information with command: {command}')
subprocess.run([command])
