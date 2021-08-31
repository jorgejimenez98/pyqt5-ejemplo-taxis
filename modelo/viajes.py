from modelo.funciones_de_ayuda import *


class Viaje:
    def __init__(self, cod_viaje, fecha_inicio, fecha_termina, num_taxi, chofer):
        self.__cod_viaje = cod_viaje
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termina = fecha_termina
        self.__num_taxi = num_taxi
        self.__chofer = chofer

    @property
    def chofer(self):
        return self.__chofer

    @chofer.setter
    def chofer(self, value):
        self.__chofer = value

    @property
    def num_taxi(self):
        return self.__num_taxi

    @num_taxi.setter
    def num_taxi(self, value):
        self.__num_taxi = value

    @property
    def fecha_termina(self):
        return self.__fecha_termina

    @fecha_termina.setter
    def fecha_termina(self, value):
        self.__fecha_termina = value

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def cod_viaje(self):
        return self.__cod_viaje

    @cod_viaje.setter
    def cod_viaje(self, value):
        self.__cod_viaje = value

    def es_cod_viaje(self, value):
        return self.__cod_viaje == value

    def importe(self):
        f1 = solo_fecha(self.__fecha_inicio)
        f2 = solo_fecha(self.__fecha_termina)
        if f1 == f2:
            resta = resta_fecha(self.__fecha_inicio, self.__fecha_termina)[0]
            x = solo_hora(resta)
            resp = duracion_min(x)
        else:
            dias = int(resta_fecha(self.__fecha_inicio, self.__fecha_termina)[0])
            x = solo_hora(resta_fecha(self.__fecha_inicio, self.__fecha_termina)[2])
            dur = dias * 24 * 60
            resp = int(duracion_min(x)) + dur
        h_in = hora_a_partir_fecha(self.__fecha_inicio)
        h_end = hora_a_partir_fecha(self.__fecha_termina)
        bol = (valor_booleano_2(h_in)) and (valor_booleano_2(h_end))
        lista = [resp, bol]
        return lista
