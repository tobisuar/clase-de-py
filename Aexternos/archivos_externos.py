from io import open

archivo_texto = open("archivo.txt","r+")#se puede cambiar la R por una W si es que se necesita escribir A de append

#print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines();

lista_texto[2]="esta linea la agrego desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()





#lineas_texto = archivo_texto.readlines()#se usa para que se guarden las lineas de texto en una lista

#print(lineas_texto[0])

#texto = archivo_texto.read()#lee el texto y la almacena en texto, tambien se puede almacenar en una lista para manipularlo mejor

#archivo_texto.close()#cerramos el lector de texto

#print(texto)#imprime el texto