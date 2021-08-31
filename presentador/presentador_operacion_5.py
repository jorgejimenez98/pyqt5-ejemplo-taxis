from modelo.funciones_de_ayuda import *
from modelo.servicio_repositorio import Servicio_Repositorio
from vista.dialogo_operacion_5 import Dialogo_5


class Presentador_Operacion_5:
    def __init__(self, rep):
        self.__repositorio = rep
        self.__servicio_repositorio = Servicio_Repositorio(self.__repositorio)

    def iniciar(self):
        self.__vista = Dialogo_5(self)
        self.__vista.show()

    def fun_mostrar_informacion(self):
        try:
            w = self.__servicio_repositorio.listado_viajes_fuera_ciudad_ordenado_x_distancia()
            self.__vista.vaciar_tabla()
            for i in w:
                x = self.__vista.tabla.rowCount()
                self.__vista.tabla.insertRow(x)
                fecha_inicio = fecha_en_cadena_a_partir_del_datetime(i[1])
                fecha_termina = fecha_en_cadena_a_partir_del_datetime(i[2])
                hab = 'No'
                if i[9]:
                    hab = 'Si'
                self.__vista.agregar_elemento_tabla(x, 0, i[0])
                self.__vista.agregar_elemento_tabla(x, 1, fecha_inicio)
                self.__vista.agregar_elemento_tabla(x, 2, fecha_termina)
                self.__vista.agregar_elemento_tabla(x, 3, i[3])
                self.__vista.agregar_elemento_tabla(x, 4, i[8])
                self.__vista.agregar_elemento_tabla(x, 5, hab)
                self.__vista.agregar_elemento_tabla(x, 6, i[4])
                self.__vista.agregar_elemento_tabla(x, 7, i[5])
                self.__vista.agregar_elemento_tabla(x, 8, i[6])
                self.__vista.agregar_elemento_tabla(x, 9, i[7])
            self.__vista.tabla.resizeColumnsToContents()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])
