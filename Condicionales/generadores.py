#def generaPares(limite):
#    num = 1
#    miLista = []
#    while num < limite:
#        miLista.append(num * 2)
#        num = num + 1

#    return miLista

#print(generaPares(10))

# Va generando pares a medida que los voy requiriendo.

# def generaPares(limite):
#     num = 1
#     while num < limite:
#         yield num * 2
#         num = num + 1
#
# pares = generaPares(10)
#
#
#
# print(next(pares))
# print("Aqui podria ir mas codigo.")
# print(next(pares))

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
        # Hace lo mismo que for subelemento in elemento.
        yield from elemento


devuelveCiudades = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(devuelveCiudades))
print(next(devuelveCiudades))
