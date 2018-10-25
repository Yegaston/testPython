from io import open

# archivo_texto = open('Fichero.txt', 'w')


# W Escribir R Leer A agregar
archivo_texto = open('Fichero.txt', 'a')

# Escritura de ficheros

# frase = "NO HAY PROBLEMA WILLY \n ME COMERE A SUERTUDO"

# archivo_texto.write(frase)

# archivo_texto.close()

# Lectura de fichero

# texto = archivo_texto.read()
# archivo_texto.close()

# print(texto)

# Esto lee y almacena como si fuera una lista.

# lineas_texto = archivo_texto.readlines()

# print(lineas_texto)

archivo_texto.write("\n ALF :D")

archivo_texto.close()