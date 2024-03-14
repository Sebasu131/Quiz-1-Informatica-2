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