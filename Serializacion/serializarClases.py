import pickle

class Vehiculos():
    def  __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True
    def frenar (self):
        self.frena = True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena)

class Moto(Vehiculos):
    hCaballito = ""
    def caballito(self):
        self.hCaballito = "Ago caballito, negro."
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena, "\n", self.hCaballito)

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada."
        else:
            return "La Furgoneta no esta cargada."

class Auto(Vehiculos):
    pass

class VeElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True

Mazda = Vehiculos("Mazda", "MX5")
Seat = Vehiculos("Seat", "Leon")
Renault = Vehiculos("Renault", "Megane")
coches =[Mazda, Seat, Renault]

fichero = open("losCoches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del(fichero)

ficheroApertura = open("losCoches" , "rb")
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
    print(c.estado())
    print("\n")