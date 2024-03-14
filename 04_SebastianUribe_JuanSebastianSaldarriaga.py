class ImplanteMedico:
    def __init__(self, tipo, material, tipo_fijacion, tamano):
        self.__tipo = tipo
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamano = tamano
    #Getters ImplanteMedico
    def vertipo(self):
        return self.__tipo
    def vermaterial(self):
        return self.__material
    def vertipofijacion(self):
        return self.__tipo_fijacion
    def vertamano(self):
        return self.__tamano
    #Setters ImplanteMedico
    def asignartipo(self,n):
        self.__tipo=n
    def asignarmaterial(self,c):
        self.__material=c
    def asignartipofijacion(self,fi):
        self.__tipo_fijacion=fi
    def asignartamano(self,M):
        self.__tamano=M

class ProtesisCadera(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamano):
        super().__init__("Prótesis de cadera", material, tipo_fijacion, tamano)

class Marcapasos(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamano, num_electrodos, alambrico, frecuencia):
        super().__init__("Marcapasos", material, tipo_fijacion, tamano)
        self.__num_electrodos = num_electrodos
        self.__alambrico = alambrico
        self.__frecuencia = frecuencia
    #Getters Marcapasos
    def verelectrodos(self):
        return self.__num_electrodos
    def veralambrico(self):
        return self.__alambrico
    def verfrecuencia(self):
        return self.__frecuencia
    #Setters Marcapasos
    def asignarelectrodos(self,n):
        self.__num_electrodos=n
    def asignaralambrico(self,c):
        self.__alambrico=c
    def asignarfrecuencia(self,fi):
        self.__frecuencia=fi
    

class StentCoronario(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamano, longitud, diametro):
        super().__init__("Stent Coronario", material, tipo_fijacion, tamano)
        self.__longitud = longitud
        self.__diametro = diametro
    #Getters StentCoronario
    def verlongitud(self):
        return self.__longitud
    def verdiametro(self):
        return self.__diametro
    #Setters StentCoronario
    def asignarlongitud(self,l):
        self.__longitud=l
    def asignardiametro(self,d):
        self.__diametro=d

class ImplanteDental(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamano, forma, sistema_fijacion):
        super().__init__("Implante Dental", material, tipo_fijacion, tamano)
        self.__forma = forma
        self.__sistema_fijacion = sistema_fijacion
    #Getters ImplanteDental
    def verforma(self):
        return self.__forma
    def versistema(self):
        return self.__sistema_fijacion
    #Setters ImplanteDental
    def asignarforma(self,f):
        self.__forma= f
    def asignarsistema(self,s):
        self.__sistema_fijacion=s

class ProtesisRodilla(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamano):
        super().__init__("Prótesis de rodilla", material, tipo_fijacion, tamano)

class Paciente:
    
    def __init__(self,nombre,cedula,fechaimplantacion,medico,estadoimp,implante):
        self.__nombre= nombre
        self.__cedula= cedula
        self.__fechaimplantacion= fechaimplantacion
        self.__medico= medico
        self.__estadoimp= estadoimp
        self.__implante= implante
    #Getters Paciente
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verFechaimplantacion(self):
        return self.__fechaimplantacion
    def verMedico(self):
        return self.__medico
    def verEstadoimp(self):
        return self.__estadoimp
    def verImplante(self):
        return self.__implante
    #Setters Paciente
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarCedula(self,c):
        self.__cedula=c
    def asignarFechaimplantacion(self,fi):
        self.__fechaimplantacion=fi
    def asignarMedico(self,M):
        self.__medico=M
    def asignarEstadoimp(self,f):
        self.__estadoimp=f
    def asignarImplante(self,i):
        self.__implante=i
class Sistema:
    def __init__(self):
        self.__inventario = []
        self.__pacientes = []

    def Verinventario(self):
        return self.__inventario
    
    def agregarImplante(self, implante):
        self.__inventario.append(implante)

    def eliminarImplante(self, implante):
        if implante in self.__inventario:
            self.__inventario.remove(implante)
            print("Implante eliminado.") 

    def ingresarPaciente(self, paciente):
        self.__pacientes.append(paciente)

    def verPacientes(self):
        return self.__pacientes

    def verificarExiste(self, cedula):
        return True if any(paciente.cedula == cedula for paciente in self.inventario) else False

    def recuperaPac(self, cedula):
        return next(paciente for paciente in self.__pacientes if paciente.cedula == cedula)
    def verPacientes(self):
        return self.__pacientes
    def imprimirInventario(self):
        for objeto in self.Verinventario:
            print(objeto)
    def imprimirPacientes(self):
        for objeto in self.verPacientes:
            print (objeto)

