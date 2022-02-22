mensaje = "hola"
mensaje += " tobi"
mensaje += " estamos asignando cosas"
"asignacion de numeros"
orden = input("CALCULADORA")
numero = int(input("INGRESE UN NUMERO"))
numero = int(input("2 INGRESE UN NUMERO"))
if orden == "+":
    numero += numero
elif orden == "-":
    numero -= numero
elif orden == "*":
    numero *= numero
elif orden == "/":
    numero /= numero
elif orden == "//":
    numero //= numero
elif orden == "**":
    numero **= numero
print(mensaje,numero)