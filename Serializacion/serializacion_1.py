import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Chizzo"]

fichero_binario = open("Listanombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del (fichero_binario)