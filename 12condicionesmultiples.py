"ingreso de palabra preservada ELIF que agrega mas instrucciones con condiciones logicas "

nombre = input("ingrese su nombre por favor... ")

matematicas = float(input("hola"+nombre+"ingrese su nota en matematicas..."))
quimica = float(input("hola"+nombre+"ingrese su nota en quimica..."))
edufisica = float(input("hola"+nombre+"ingrese su nota en educacion fisica... "))

if matematicas == 10:
    print(nombre + "sos un capo de la matematica")
elif quimica == 10:
    print(nombre + "sos un capo de la quimica hermano")
elif edufisica == 10:
    print(nombre+ "sos alto deportista")
else:
    print("por lo menos aprobaste las materias no? ._.XD")