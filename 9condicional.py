nombre = input("cual es tu nombre ")
nota1 = int(input("ingrese el valor de tu primer nota "))
nota2 = int(input ("ingrese el valor de tu segunda nota "))
nota3 = int(input("ingrese el valor de tu tercer nota "))

promedio = (nota1 + nota2 + nota3)/3

if promedio > 5:
    print("aprobaste con ", promedio, " ",nombre)
    