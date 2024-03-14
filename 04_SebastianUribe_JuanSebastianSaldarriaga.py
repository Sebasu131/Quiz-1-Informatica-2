class ImplanteMedico:
    def __init__(self, tipo, material, tipo_fijacion, tamano):
        self.__tipo = tipo
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamano = tamano
    def vertipo(self):
        return self.__tipo
    def vermaterial(self):
        return self.__material
    def vertipofijacion(self):
        return self.__tipo_fijacion
    def vertamano(self):
        return self.__tamano
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
    def verelectrodos(self):
        return self.__num_electrodos
    def veralambrico(self):
        return self.__alambrico
    def verfrecuencia(self):
        return self.__frecuenciaç

class StentCoronario(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamano, longitud, diametro):
        super().__init__("Stent Coronario", material, tipo_fijacion, tamano)
        self.__longitud = longitud
        self.__diametro = diametro
    def verlongitud(self):
        return self.__longitud
    def verdiametro(self):
        return self.__diametro

class ImplanteDental(ImplanteMedico):
    def __init__(self, material, tipo_fijacion, tamano, forma, sistema_fijacion):
        super().__init__("Implante Dental", material, tipo_fijacion, tamano)
        self.__forma = forma
        self.__sistema_fijacion = sistema_fijacion
    def verforma(self):
        return self.__forma
    def versistema(self):
        return self.__sistema_fijacion