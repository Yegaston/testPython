print("Evaluacion de notas de alumnos")

notaAlumno=input()

def evaluacion(nota):
    valoracion = "aprobado"
    if nota <= 5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(notaAlumno)))


numA = int(input("Introduce un numero: "))


if numA > 0:
    print("El numero es mayor a 0")
elif numA < 0:
    print("El numero es menor a 0")
else:
    print("El numero es 0.")
