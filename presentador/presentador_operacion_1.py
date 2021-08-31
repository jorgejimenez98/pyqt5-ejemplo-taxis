from modelo.servicio_repositorio import Servicio_Repositorio
from vista.dialogo_operacion_1 import Dialogo_1


class Presentador_Operacion_1:
    def __init__(self, rep):
        self.__repositorio = rep
        self.__servicio_repositorio = Servicio_Repositorio(self.__repositorio)

    def iniciar(self):
        self.__vista = Dialogo_1(self)
        self.__vista.show()

    def fun_mostrar_informacion(self):
        try:
            self.__vista.validar_operacion()
            cod = self.__vista.valor_cod_viaje
            res = self.__servicio_repositorio.importe_x_codigo_viaje(cod)
            self.__vista.mostrar_informacion(res, cod)
            self.__vista.valor_cod_viaje = ''
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
