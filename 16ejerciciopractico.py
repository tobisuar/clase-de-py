""" Solicita un sistema que determine los dias de vacaciones a los que tiene derecho un trabajador, tomando en cuenta las siguientes caracteristicas:
existen 3 departamentos con distintas claves 1. 2 y 3 
clave 1 . con 1 año de serv 6 dias de vacas, con 2 a 6, 14 dias y de 7+ 20 
clave 2. con 1 año de servicio 7 dias, con 2 a 6, 15 dias y de 7+ 22
clave 3. con 1 año 10 dias de 2 a 6 20 dias y de 7+ 30 dias 

se debe solicitar nombre, clave y antiguiedad desde el teclado dando el resumen que contenga el nombre del trabajador y los dias de vacaciones """

nombre = input("ingrese el nombre y apellido del empleado: ")
clave = int (input("ingrese clave del sujeto: "))
antiguedad = int (input("ingrese la cantidad de años de servicio: "))

if clave == 1 and antiguedad > 0:
    if antiguedad == 1:
        print("señor ",nombre,"usted posee 6 dias de vacaciones ")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("señor ",nombre, "usted posee 14 dias de vacaciones ")
    else:
        print("señor ",nombre, "usted posee 20 dias de vacaciones ")

if clave == 2 and antiguedad > 0:
    if antiguedad == 1:
        print("señor ",nombre,"usted posee 7 dias de vacaciones ")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("señor ",nombre, "usted posee 15 dias de vacaciones ")
    else:
        print("señor ",nombre, "usted posee 21 dias de vacaciones ")

if clave == 3 and antiguedad > 0:
    if antiguedad == 1:
        print("señor ",nombre,"usted posee 10 dias de vacaciones ")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("señor ",nombre, "usted posee 20 dias de vacaciones ")
    else:
        print("señor ",nombre, "usted posee 30 dias de vacaciones ")

if antiguedad == 0:
    print("no posee vacaciones.")