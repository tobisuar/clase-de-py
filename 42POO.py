#clase
class Coche():
    #metodo constructor
    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #CON ESTO ESTAMOS ENCAPSULANDO, OSEA QUE NO SE PERMITE CAMBIAR
        self.__enmarcha = False

#que es self? self hace referencia al propio objeto perteneciente a la clase
#esto es una instancia
    def arrancar (self,arrancamos):#se hace true asi que llama al chequeo y se fija si da positivo
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo = self.__chequeointerno()

        if(self.__enmarcha and chequeo):
            
            return "el coche esta en marcha"
        elif(self.__enmarcha and chequeo == False):
            if self.gasolina != "ok":
                return "no tiene gasolina"
            elif self.aceite != "ok":
                return "no tiene aceite"
            elif self.puertas == "abiertas":
                return "las puertas quedaron abiertas"
            
            return "algo esta mal en el chequeo interno"
            
        else:
            
            return "el coche esta parado"
    
    def estado(self):
        print("el coche tiene", self.__ruedas,"ruedas Un ancho de ",self.__anchoChasis," y chasis de ",self.__anchoChasis)
    
    def __chequeointerno(self):
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        
        else:
            return False


#instanciamos una clase.
miCoche = Coche()

print(miCoche.arrancar(True))#tenemos que imprimir el metodo ya que devuelve un string como "el coche esta en marcha"

miCoche.estado()

print(" a continuacion se crea el siguiente objeto-----------------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))#false se almacena en arrancamos

miCoche2.__ruedas=5

miCoche2.estado()#esta imprimiendo datos asi que va sin print