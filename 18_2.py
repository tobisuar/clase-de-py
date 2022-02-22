"""ingresar numero a travez del teclade y de esta manera se debera determinar e indicar """

numero1 = int(input("ingresar el 1er numero : "))
numero2 = int(input("ingresar el 2do numero : "))
numero3 = int(input("ingresar el 3er numero : "))

if numero1 > numero2 and numero1 > numero3:
    print("numero uno es mayor")
else: 
    if numero2 > numero3:
        print("numero 2 es mayor")
    
    else:
        print("numero 3 es mayor")