nombreUsuario = input("Ingrese el nombre del usuario: ")
print("El nombre es: ", nombreUsuario)

print("El nombre es: ", nombreUsuario.capitalize())

print("#### #### ####")

edad = input("Introduce tu edad: ")

if(edad.isdigit() == True):
    if(int(edad) >= 18):
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("Ingrese un valor numerico")


