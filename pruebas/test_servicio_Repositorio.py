from unittest import TestCase
from modelo.repositorio import Repositorio
from modelo.servicio_repositorio import Servicio_Repositorio
from modelo.viaje_local import Viaje_Local
from modelo.viaje_fuera_ciudad import Viaje_Fuera_Ciudad
from modelo.chofer import Chofer
from datetime import datetime, date


class TestServicio_Repositorio(TestCase):
    def setUp(self):
        r = Repositorio()
        self.s = Servicio_Repositorio(r)

        c1 = Chofer("Juan", 'M', 20, 25)
        c2 = Chofer("Pedro", "M", 25, 30)
        c3 = Chofer("Juanita", 'F', 30, 29)
        c4 = Chofer("Mario", 'M', 27, 31)
        c5 = Chofer("Mariano", 'M', 77, 15)
        c6 = Chofer("Pedro", 'M', 78, 40)

        v = Viaje_Local('10-xs', datetime(2018, 10, 7, 7, 0), datetime(2018, 10, 7, 7, 20), 14, c1, 5, False, True)
        v1 = Viaje_Local('14-xs', datetime(2018, 10, 7, 7, 0), datetime(2018, 10, 9, 7, 25), 15, c2, 3, True, True)
        v2 = Viaje_Local('25-xs', datetime(2018, 10, 7, 7, 0), datetime(2018, 10, 9, 7, 30), 10, c3, 2, True, False)

        v3 = Viaje_Fuera_Ciudad('58-wq', datetime(2018, 10, 8, 12, 10), datetime(2018, 10, 9, 10, 11), 11, c4, 100,
                                True)
        v4 = Viaje_Fuera_Ciudad('14-tr', datetime(2018, 11, 9, 10, 9), datetime(2018, 11, 10, 11, 9), 9, c5, 150, False)
        v5 = Viaje_Fuera_Ciudad('87-tr', datetime(2018, 12, 10, 9, 8), datetime(2018, 12, 10, 9, 10), 18, c6, 200,
                                False)

        r.lista_viajes.extend([v, v1, v2, v3, v4, v5])

    def test_importe_x_codigo_viaje(self):
        self.assertEqual(self.s.importe_x_codigo_viaje('10-xs'), 70.0)

    def test_prom_edad_chferes__viajes_locales_pas_embote_x_fecha(self):
        self.assertEqual(self.s.prom_edad_chferes__viajes_locales_pas_embote_x_fecha(date(2018, 10, 8)), 25.0)

    def test_porciento_viajes_locales_q_hicieron_por_servicio_taxi(self):
        self.assertEqual(self.s.porciento_viajes_locales_q_hicieron_por_servicio_taxi(), 66.67)

    def test_datos_viaje_local_mayor_duracion_x_fecha(self):
        self.assertEqual(self.s.datos_viaje_local_mayor_duracion_x_fecha(date(2018, 10, 8)),
                         ['25-xs', datetime(2018, 10, 7, 7, 0), datetime(2018, 10, 9, 7, 30), 10,
                          'Juanita', 'F', 30, 29, 2, True, False])

    def test_listado_viajes_fuera_ciudad_ordenado_x_distancia(self):
        self.assertEqual(self.s.listado_viajes_fuera_ciudad_ordenado_x_distancia(), [
            ['14-tr', datetime(2018, 11, 9, 10, 9), datetime(2018, 11, 10, 11, 9), 9, 'Mariano', 'M', 77, 15, 150,
             False],
            ['87-tr', datetime(2018, 12, 10, 9, 8), datetime(2018, 12, 10, 9, 10), 18, 'Pedro', 'M', 78, 40, 200,
             False]])
