class persona():
    
    def __init__(self,nombre,dni,edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
    
    def descripcion (self):
        print("Nombre: ", self.nombre,"DNI: ",self.dni,"Edad: ",self.edad)

class empleado(persona):

    def __init__(self,sueldo,horario,antiguedad,nombre,dni,edad):

        super().__init__(nombre,dni,edad)

        self.sueldo = sueldo
        self.horario = horario
        self.antiguiedad = antiguedad

class estudios(empleado,persona):

    def __init__(self,primaria,secundario,universidad,cursos,sueldo,horario,antiguedad,nombre,dni,edad):

        super().__init__(nombre,dni,edad,sueldo,horario,antiguedad)
        self.primaria = primaria
        self.secundario = secundario
        self.universidad = universidad
        self.cursos = cursos
    def est(self):
        print("tiene estudios universitarios??", self.universidad)
        
Damian = estudios("si","si","si","ninguno","40000","8hrs","5 años","tobias","42428760","21")
Damian.descripcion()
Damian.est()