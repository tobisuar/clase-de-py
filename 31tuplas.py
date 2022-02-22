#las tuplas no permiten realizar busquedas ni añadir elementos en una lista. 
# las ventajas de una tupla es la rapidez al momento de la ejecucion ocupando siempre menos espacio en memoria que una lista.
#por ejemplo es utilizada en elementos que no vamos a tener que modificar, permitiendonos formateando strings y agregando en claves en un diccionario

tupla = ("se", "puede usar","con")
tupla2 = "o", "sin", "parentesis"

print(tupla[1])

#transformar tupla a lista

lista=list(tupla)
lista.append (" transformada en una lista")
print(tupla2)
print(lista)
#transformar tupla en lista

tupla = tuple(lista)

tupla.index("se")