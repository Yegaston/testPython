import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        print("Se ha creado una persona nueva con el nombre de " , self.nombre)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("FicheroPersonas", "ab+")
        listaDePersonas.seek(0)

        try:     
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersonas(self, p):
        self.personas.append(p)
        self.GuardarEnFichero()
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
        
    def GuardarEnFichero(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFichero(self):
        print("La informacion del fichero es la siguiente:")
        for p in self.personas:
            print(p)

miLista = ListaPersonas()

persona = Persona("Eminem", "Masculino", 49)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFichero()

# p = Persona("Gaston", "Masculino", 29)
# miLista.agregarPersonas(p)
# p = Persona("Marilina", "Femenina", 28)
# miLista.agregarPersonas(p)
# p = Persona("Lautaro", "Masculino", 19)
# miLista.agregarPersonas(p)

# miLista.mostrarPersonas()