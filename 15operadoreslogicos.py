numero = int(input("ingrese un numero "))
numero2 = int(input("ingrese un numero "))
if numero > 10 and numero2 >= 10:
    total = numero - numero2
    print (total)
elif numero < 10 and numero2 < 10:
    total = numero + numero2
    print(total)