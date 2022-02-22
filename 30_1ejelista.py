#hacer un programa donde se pueda agregar personal y dias de vacaciones si este no tiene

from typing import Container


empleados = []
nuevoemp = ""
vacaciones = []
agregarvac = ""
contador = 6
while contador < 10:
    nuevoemp = input ("ingresar en la siguiente el nombre del empleado: ")
    agregarvac = input ("ingresar la cantidad de dias de vacaciones")
    empleados.append (nuevoemp)
    vacaciones.append (agregarvac)
    contador +=1


"""la forma de agregar items a la lista son append, extend y remove """

print(empleados[:])
print(vacaciones[:])