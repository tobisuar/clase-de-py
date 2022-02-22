diccionario = { }
num = 0

while num != 5 :
    empleado = input("ingrese el empleado que quiere agregar a la Lista ")
    if empleado == "ninguno":
        num = 4
    else:
        diccionario [num] = empleado
    num +=1

print(diccionario)