from PyQt5.QtWidgets import QApplication
from modelo.repositorio import Repositorio
from modelo.servicio_repositorio import Servicio_Repositorio
from vista.ventana_principal import Main_Window
from presentador.presentador_viaje_local import Presentador_Viaje_Local
from presentador.presentador_viaje_fuera_ciudad import Presentador_Viaje_Fuera_Ciudad
from presentador.presentador_operacion_1 import Presentador_Operacion_1
from presentador.presentador_operacion_2 import Presentador_Operacion_2
from presentador.presentador_operacion_3 import Presentador_Operacion_3
from presentador.presentador_operacion_4 import Presentador_Operacion_4
from presentador.presentador_operacion_5 import Presentador_Operacion_5
import sys


class Presentador_Principal:
    def __init__(self):
        self.__repositorio = Repositorio()
        self.__servicio_repositorio = Servicio_Repositorio(self.__repositorio)

    def iniciar(self):
        self.__app = QApplication(sys.argv)
        self.__vista = Main_Window(self)
        self.__vista.show()
        self.__app.exec_()

    def CRUD_viaje_local(self):
        ven = Presentador_Viaje_Local(self.__repositorio)
        ven.iniciar()

    def CRUD_viaje_fuera_ciudad(self):
        ven = Presentador_Viaje_Fuera_Ciudad(self.__repositorio)
        ven.iniciar()

    def mostrar_operacion_1(self):
        ven = Presentador_Operacion_1(self.__repositorio)
        ven.iniciar()

    def mostrar_operacion_2(self):
        ven = Presentador_Operacion_2(self.__repositorio)
        ven.iniciar()

    def mostrar_operacion_3(self):
        ven = Presentador_Operacion_3(self.__repositorio)
        ven.iniciar()

    def mostrar_operacion_4(self):
        ven = Presentador_Operacion_4(self.__repositorio)
        ven.iniciar()

    def mostrar_operacion_5(self):
        ven = Presentador_Operacion_5(self.__repositorio)
        ven.iniciar()
