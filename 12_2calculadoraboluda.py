"intento de hacer calculadora automatica"
numero1 = float(input("ingresar el primer numero: "))
simbolo = input("ingrese simbolo *,%,/,+ o -")
numero2 = float(input("ingresa el segundo numero: "))

if simbolo == "*":
    total = numero1 * numero2
elif simbolo == "/":
    total = numero1 / numero2
elif simbolo == "%":
    total = numero1 % numero2
elif simbolo == "+":
    total = numero1 + numero2
elif simbolo == "-":
    total = numero1 - numero2

print(total)
