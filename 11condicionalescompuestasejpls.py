print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar ingrese su nombre...")

matematicas = float(input(nombre + "ingrese la nota de matematicas..."))
quimica = float(input(nombre + "ingrese la calificacion de quimica ..."))
biologia = float(input(nombre + "ingrese la calificacion en biologia..."))

promedio = (matematicas + quimica + biologia )/3

if promedio >= 6:
    print(" aprobaste rey bien ahi " + nombre + ' " es hora de correr de casa con un promedio de " ',round(promedio,2))
else:
    print("es hora de correr... tenes un promedio de  ",round(promedio,2))
