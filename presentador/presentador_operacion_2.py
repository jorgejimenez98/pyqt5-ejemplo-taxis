from modelo.servicio_repositorio import Servicio_Repositorio
from vista.dialogo_operacion_2 import Dialogo_2
from datetime import date


class Presentador_Operacion_2:
    def __init__(self, rep):
        self.__repositorio = rep
        self.__servicio_repositorio = Servicio_Repositorio(self.__repositorio)

    def iniciar(self):
        self.__vista = Dialogo_2(self)
        self.__vista.show()

    def fun_mostrar_informacion(self):
        try:
            fecha = self.__vista.valor_fecha
            res = self.__servicio_repositorio.prom_edad_chferes__viajes_locales_pas_embote_x_fecha(fecha)
            self.__vista.mostrar_informacion(str(res))
            self.__vista.valor_fecha = date(2018, 1, 1)
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
