from modelo.viajes import Viaje


class Viaje_Local(Viaje):
    def __init__(self, cod_viaje, fecha_inicio, fecha_termina, num_taxi, chofer, cant_pasajaros, fue_servicio_recorrida,
                 paso_embotellamineto):
        Viaje.__init__(self, cod_viaje, fecha_inicio, fecha_termina, num_taxi, chofer)
        self.__cant_pasajaros = cant_pasajaros
        self.__fue_servicio_recorrida = fue_servicio_recorrida
        self.__paso_embotellamineto = paso_embotellamineto

    @property
    def paso_embotellamineto(self):
        return self.__paso_embotellamineto

    @paso_embotellamineto.setter
    def paso_embotellamineto(self, value):
        self.__paso_embotellamineto = value

    @property
    def fue_servicio_recorrida(self):
        return self.__fue_servicio_recorrida

    @fue_servicio_recorrida.setter
    def fue_servicio_recorrida(self, value):
        self.__fue_servicio_recorrida = value

    @property
    def cant_pasajaros(self):
        return self.__cant_pasajaros

    @cant_pasajaros.setter
    def cant_pasajaros(self, value):
        self.__cant_pasajaros = value

    def importe(self):
        i = Viaje.importe(self)
        if i[1]:
            return i[0] * 3.50
        else:
            return i[0] * 5.50
