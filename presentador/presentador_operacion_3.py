from modelo.servicio_repositorio import Servicio_Repositorio
from vista.dialogo_operacion_3 import Dialogo_3


class Presentador_Operacion_3:
    def __init__(self, rep):
        self.__repositorio = rep
        self.__servicio_repositorio = Servicio_Repositorio(self.__repositorio)

    def iniciar(self):
        self.__vista = Dialogo_3(self)
        self.__vista.calculo()

    def fun_mostrar_informacion(self):
        try:
            res = self.__servicio_repositorio.porciento_viajes_locales_q_hicieron_por_servicio_taxi()
            self.__vista.mostrar_informacoion(res)
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
