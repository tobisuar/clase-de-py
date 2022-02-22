
def evaluacion (edad):
    if edad < 0:
        raise TypeError ("no se permiten edades menores a 0")
    elif edad < 20:
        return print("eri joven ctm")
    elif edad < 40:
        return print("eri adulto ctm")
    elif edad < 65:
        return print("tas medio pelo")
    elif edad < 1000:
        return print("wtf tremendo goku")
while True:
    try:
        evaluacion(int(input("ingrese una edad")))
    except ValueError:
        print("capo no metas un string en esa parte mete un numero")