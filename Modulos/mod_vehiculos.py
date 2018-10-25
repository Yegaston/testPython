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

# miMoto = Moto("Honda", "CBR")
# miMoto.arrancar()
# miMoto.caballito()
# miMoto.estado()

# print("\n\n")

# miAuto = Auto("Renault", "Corsa")
# miAuto.estado()

# print("\n\n")

# miFurgoneta = Furgoneta("Tesla", "Cargoster")

# miFurgoneta.arrancar()
# miFurgoneta.estado()
# print(miFurgoneta.carga(True))

# class BicicletaElectrica(VeElectricos, Vehiculos):
#     pass

# miBici = BicicletaElectrica("Mona", "Xdedx")




