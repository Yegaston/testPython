import pickle

fichero = open("Listanombres", 'rb')

lista = pickle.load(fichero)

print(lista)