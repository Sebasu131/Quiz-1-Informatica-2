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
def validar(mens): #se añade funcion para validar los datos numericos del menú
    while True:
        try:
            valor = int(input(mens))
            break
        except ValueError:
            print("Ingresar un número entero")
            continue
    return valor
def main():
        sis=Sistema()
        while True:
            print("1. Ingresar nuevo implante\n 2. Editar informacion de implante existente\n 3. Eliminar implante\n 4. Mostrar todo el inventario\n5.")
            valor=validar("Valor: ")
            if valor ==1: #ingresar nuevo implante
                cedula = input("Ingrese la cédula del paciente: ")
                material=input("Ingrese el material: ")
                tipo_fijacion=input("Ingrese el tipo de fijación: ")
                tamano=input("Ingrese el tamaño del implante: ")
                while True:
                    opc=validar("Ingrese el tipo de implante:\n1. Implante dental\n2. Marcapasos\n3. Protesis de cadera\n4. Protesis de rodilla\n5. Stent coronario\n6. Salir\n")
                    if opc == 1:
                        forma=input("Ingrese la forma del implante dental: ")
                        sistema_fijacion=input("Ingrese el sistema de fijación: ")
                        implante=ImplanteDental(material,tipo_fijacion,tamano,forma,sistema_fijacion)
                        sis.agregarImplante(implante)#implante dental
                    elif opc == 2:
                        num_electrodos = input("Ingrese el número de electrodos: ")
                        alambrico= input("Alámbrico o inalámbrico: ")
                        frecuencia=input("Ingrese la frecuencia del marcapasos: ")
                        implante = Marcapasos(material,tipo_fijacion,tamano,num_electrodos,alambrico,frecuencia)
                        sis.agregarImplante(implante)
                        #marcapasos
                    elif opc==3:#protesis de cadera
                        implante=ProtesisCadera(material,tipo_fijacion,tamano)
                        sis.agregarImplante(implante)#protesis de cadera
                    elif opc==4:
                        implante=ProtesisRodilla(material,tipo_fijacion,tamano)#protesis de rodilla
                        sis.agregarImplante(implante)
                        #protesis de rodilla
                    elif opc==5:
                        longitud=input("Ingresa la longitud del stent coronario: ")
                        diametro=input("Ingresa el diámetro del stent coronario: ")
                        implante=StentCoronario(material,tipo_fijacion,tamano,longitud,diametro)
                        sis.agregarImplante(implante)
                        #stent coronario
                    elif opc==6: #salida
                        break
                    else:
                        print('ingrese una opción válida')
                        continue
            elif valor ==2: #editar implante existente
                while True:
                    opc = validar("Menú de Edición - Ingrese el tipo de implante a editar:\n1. Implante Dental\n2. Marcapasos\n3. Prótesis de Cadera\n4. Prótesis de Rodilla\n5. Stent Coronario\n6. Salir\n")

                    if opc == 1:
                        nombre_implante = "Implante Dental"
                        break
                    elif opc == 2:
                        nombre_implante = "Marcapasos"
                        break
                    elif opc == 3:
                        nombre_implante = "Prótesis de Cadera"
                        break
                    elif opc == 4:
                        nombre_implante = "Prótesis de Rodilla"
                        break
                    elif opc == 5:
                        nombre_implante = "Stent Coronario"
                        break
                    elif opc == 6:
                        break
                    else:
                        print('Ingrese una opción válida')
                        continue
            elif valor ==3: #eliminar implante existente
                  continue
            elif valor ==4: #mostrar todo el inventario
                  continue
            elif valor==5:
                  break
            
