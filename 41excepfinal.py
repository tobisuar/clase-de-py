import math

def calculaRaiz (num1):
    if num1 <0:
        raise ValueError ("el numero no puede ser negativo. ")
    else:
        return math.sqrt(num1)

operacion =(int(input("ingrese un numero: ")))
try:
    print(calculaRaiz(operacion))
except ValueError as Errordenumeronegativo:
    print(Errordenumeronegativo)
print("programa finalizado")