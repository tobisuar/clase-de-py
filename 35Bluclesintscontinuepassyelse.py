for letra in "python":
    if letra == "h":
        continue
    print("escritura de la letra", letra )
correo = input("ingrese el correo electronico: ")
contador = 0

for mail in correo:
    if mail == "@":
        contador = contador +1

if contador == 2:
    print(" No se puede ingresar mas de un @ vuelva a ingresar el mail ")
else:
    print("el mail se ingreso correctamente")
