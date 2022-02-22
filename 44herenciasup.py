class persona():
    def __init__ (self,nombre,edad,lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    def descripcion(self):

        print("Nombre: ",self.nombre,"edad: ",self.edad,"residencia: ",self.lugar_residencia)

class empleado(persona): #principio de sustitucion, cuando tenemos herencia un objeto de una clase siempre va a ser algo de la superclase es el "principio de sustitucion"

    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)#construte al metodo de la clase padre sin necesidad de declarar
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()
        print("salario de ",self.salario,"antiguedad de ",self.antiguedad)

antonio = empleado(1500,5,"tobias",21,2) 

antonio.descripcion()

print(isinstance(antonio,persona))