class Coche():
    
    def __init__(self):

        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4
        self.enMarcha = False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)
    
        
            
Citroen = Coche()

print(Citroen.arrancar(True))

Citroen.estado()

print(" ######## Segundo Objeto ########")

Renault = Coche()

print(Renault.arrancar(False))

Renault.ruedas = 5

Renault.estado()