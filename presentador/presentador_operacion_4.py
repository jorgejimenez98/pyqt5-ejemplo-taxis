from modelo.servicio_repositorio import Servicio_Repositorio
from vista.dialogo_operacion_4 import Dialogo_4
from datetime import date


class Presentador_Operacion_4:
    def __init__(self, rep):
        self.__repositorio = rep
        self.__servicio_repositorio = Servicio_Repositorio(self.__repositorio)

    def iniciar(self):
        self.__vista = Dialogo_4(self)
        self.__vista.show()

    def fun_mostrar_informacion(self):
        try:
            fecha = self.__vista.valor_fecha
            i = self.__servicio_repositorio.datos_viaje_local_mayor_duracion_x_fecha(fecha)
            cod, fecha_inicio, fecha_termina, num_taxi, nombre, llamada, emb = i[0], i[1], i[2], i[3], i[4], i[9], i[10]
            llam = 'No'
            if llamada:
                llam = 'Si'
            em = 'No'
            if emb:
                em = 'Si'
            self.__vista.mostrar_informacion(fecha, cod, fecha_inicio, fecha_termina, num_taxi, nombre, llam, em)
            self.__vista.valor_fecha = date(2018, 1, 1)
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
