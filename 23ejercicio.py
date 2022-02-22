"imprimir en pantalla la sucesion de fibonacci desde el numero 0 hasta el numero 1597 de manera horizontal"
numero1 = 0
numero2 = 1
while numero1 <= 1597:
    print (numero1,numero2, end=" ")
    numero1 = numero1 + numero2
    numero2 = numero1 + numero2