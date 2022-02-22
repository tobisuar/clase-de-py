"""desarrollar un programa que solicite un numero entero desde teclado al usuario, posteriormente, el programa debera determinar e 
indicar a traves de un mensaje, si el numero introducido es par o impar """

numero = int(input("ingrese un numero: "))

resto = numero % 2
if resto == 1 :
    print("el numero es impar")
else:
    print("el numero es par ")