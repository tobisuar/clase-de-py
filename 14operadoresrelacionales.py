print("vamos a probar los operadores racionales ")

numero = float(input("ingrese un numero para comparar "))
numero1 = float(input("ingrese otro numero para comparar"))

if numero != 0:
    print("el numero es distinto a 0")
    if numero > numero1:
        print("el numero ",numero,"es mayor")
    else:
        print("el numero es menor a ",numero1)

else:
    print("el numero es 0")
    