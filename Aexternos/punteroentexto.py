from io import open

archivo_texto = open("archivo.txt","r+")#lectura y escritura

#rchivo_texto.write("pos vamos a ver XD ")

lista_texto = archivo_texto.readlines();

lista_texto[1] = "esta linea de texto la depositamos en el nro 10 \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)


#archivo_texto.seek(len(archivo_texto.read())/2)#modifica la ubicacion del puntero

#print(archivo_texto.read())#ubicando ()se puede colocar las barras donde se necesite
