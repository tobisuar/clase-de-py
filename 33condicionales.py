


def evaluacion (nota):
    valoracion ="aprobado"
    if nota < 5:
        valoracion = "Desaprobado"
    return valoracion

valor = int(input("ingrese la nota de un alumno "))

print(evaluacion(valor))