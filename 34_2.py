import math

print("programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero: "))

intentos = 0

while numero < 0:
    print("no se puede hallar la raiz de un numero negativo o 0")

    if intentos == 2:
        print("consumiste muchos intentos")
        break
    numero = int(input("introduce un numero por favor: "))
    if numero < 0:
        intentos = intentos+1
    
if intentos < 2:
    solucion = math.sqrt(numero)
    print("la raiz cuadrada de "+str(numero)+" es "+str(solucion))

    