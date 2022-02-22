import pickle


class vehiculo():#clase

    def __init__(self,marca,modelo):#constructor
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelerar = False
        self.frenar = False
    
    def arrancar(self):#metodos

        self.enmarcha = True

    def acelerar(self):
    
        self.acelerar = True
    
    def frenar(self):
        self.frenar = True
    def estado(self):

        print("marca: ",self.marca,"\nModelo:",self.modelo,"\nEnmarca",self.enmarcha,"\nAcelerar",self.acelerar,"\nFrenar",self.frenar)

class Furgoneta(vehiculo):

    def carga(self,cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada "
        else:
            return "La furgoneta no esta cargada "

class moto(vehiculo):#hereda vehiculos por lo tanto tiene el constructor
    hacercaballito = ""
    def caballito(self):#metodo propio
        self.hacercaballito = "voy haciendo caballito"

    def estado(self):
        print("marca: ",self.marca,"\nModelo:",self.modelo,"\nEnmarca",self.enmarcha,"\nAcelerar",self.acelerar,"\nFrenar",self.frenar, "\ncaballito ",self.hacercaballito)

class quad (moto):
    pass

class electricos (vehiculo):
    def __init__(Self,marca,modelo):

        super().__init__(self,marca,modelo)

        self.autonomia = 100

    def cargarEnergia(self):

        self.cargando = True


coche1= vehiculo("ferrari","de XD")

coche2= vehiculo("seatr","de tobi")

coche3= vehiculo("reana","de tobisuar")

coches = [coche1,coche2,coche3]

fichero = open("losCoches", "wb")

pickle.dump(coches,fichero)

fichero.close()

del (fichero)

ficheroapertura = open("losCoches","rb")

misCoches=pickle.load(ficheroapertura)

ficheroapertura.close()

for c in misCoches:
    print(c.estado())
