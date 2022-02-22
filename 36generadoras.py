def generarPares (limite):
    num = 1

    miLista = []

    while num < limite:
        yield num*2
        num=num+1
devuelvePares = generarPares(10)

print(next(devuelvePares))

print("aca podria ir mas codigo")

print(next(devuelvePares))

#entre llamada y llamada el objeto generador entra en un estado de suspencion que hace que se ahorre recursos