class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
    def descripcion(self):
        print("\nNombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.residencia)

class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion()
        print("\nSalario: ", self.salario, "\nAntiguedad: ", self.antiguedad)


Gaston = Empleado(15000, 12, "Gaston", "29", "Rosario")

Gaston.descripcion()

Manuel = Persona("Manuel", 13, "Rosario")


Manuel.descripcion()
print(isinstance(Manuel, Empleado))