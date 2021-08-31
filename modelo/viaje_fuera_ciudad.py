from modelo.viajes import Viaje


class Viaje_Fuera_Ciudad(Viaje):
    def __init__(self, cod_viaje, fecha_inicio, fecha_termina, num_taxi, chofer, distancia_klm, si_chofer_habilito):
        Viaje.__init__(self, cod_viaje, fecha_inicio, fecha_termina, num_taxi, chofer)
        self.__distancia_klm = distancia_klm
        self.__si_chofer_habilito = si_chofer_habilito

    @property
    def si_chofer_habilito(self):
        return self.__si_chofer_habilito

    @si_chofer_habilito.setter
    def si_chofer_habilito(self, value):
        self.__si_chofer_habilito = value

    @property
    def distancia_klm(self):
        return self.__distancia_klm

    @distancia_klm.setter
    def distancia_klm(self, value):
        self.__distancia_klm = value

    def importe(self):
        i = Viaje.importe(self)
        if i[1]:
            return i[0] * 3.50
        else:
            return (i[0] * 5.50) + (2 * self.__distancia_klm)

    def __gt__(self, other):
        return self.__distancia_klm > other.distancia_klm

    def es_si_chofer_habilito(self, value):
        return self.__si_chofer_habilito == value
