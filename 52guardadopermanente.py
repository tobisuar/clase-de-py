import pickle
class persona:

    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad = edad
        print("se genero una persona nueva",self.nombre)
    
    def __str__(self):
        return "{} {} {} ".format(self.nombre,self.genero,self.edad)

class listaPersonas:

    persona=[]
    def __init__(self):
        
        listaDePersonas=open("ficheroExterno","ab+")
        listaDePersonas.seek(0)

        try:

            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personad del fichero externo".format(len(self.personas)))
        
        except:
            print("El fichero esta vacio")
        
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self,p):
        self.persona.append(p)
    
    def mostrarPersonas(self):
        for p in self.persona:
            print(p)

    def guardarPersonasEnFicheroExterno(self):#uso de guardado permanente
        listaDePersonas = open("ficheroExterno","wb")#abrimos el archivo de ficheros
        pickle.dump(self.personas,listaDePersonas)#ingresamos a la persona a la lista
        listaDePersonas.close()#cerramos la lista
        del(listaDePersonas)#eliminamos el proceso para que no ocupe espacio

    def mostrarInfoFicheroExterno (self):
        print("mostramos los siguientes datos")
        for p in self.persona:
            print (p)

    def mostrarInfo(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.persona:
            print(p)

miLista=listaPersonas()

Persona = persona("daniel","persona","2121")#ingresamos la persona
miLista.agregarPersonas(Persona)#la agregamos
miLista.mostrarInfo()#mostramos la info
miLista.mostrarInfoFicheroExterno()