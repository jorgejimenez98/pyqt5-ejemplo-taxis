class Chofer:
    def __init__(self, nombre, sexo, edad, experiencia):
        self.__nombre = nombre
        self.__sexo = sexo
        self.__experiencia = experiencia
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, value):
        self.__experiencia = value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, value):
        self.__sexo = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
