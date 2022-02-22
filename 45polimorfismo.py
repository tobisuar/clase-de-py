class coche():

    def desplazamiento(self):
        print("me desplazo usando 4 ruedas")

class moto():

    def desplazamiento(self):
        print("me desplazo usando 2 ruedas")

class camion():

    def desplazamiento(self):
        print("me desplazo usando 6 ruedas")

def desplazamientovehiculo (vehiculo):#como un vehiculo puede cambiar de forma en cualquier momento podemso ver a que objeto va a desplazar
    vehiculo.desplazamiento()

mivehiculo = camion()
desplazamientovehiculo(mivehiculo)#sabe que tiene que llamar al objeto de tipo camion