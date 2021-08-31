from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtGui import QPixmap, QBrush, QResizeEvent, QPalette
from PyQt5.QtCore import Qt
from PyQt5 import uic
from datetime import date
import ctypes


class Main_Window(QMainWindow):
    def __init__(self, presentador):
        QMainWindow.__init__(self)
        uic.loadUi('vista/ui/main_window.ui', self)
        self.__presentador = presentador

        self.annadir_eventos()
        self.mover_al_medio()
        self.annadir_titulo()

    def annadir_eventos(self):
        self.ac_close.triggered.connect(self.close)
        self.ac_viaje_local.triggered.connect(self.__presentador.CRUD_viaje_local)
        self.ac_viaje_ciudad.triggered.connect(self.__presentador.CRUD_viaje_fuera_ciudad)
        self.ac_op1.triggered.connect(self.__presentador.mostrar_operacion_1)
        self.ac_op2.triggered.connect(self.__presentador.mostrar_operacion_2)
        self.ac_op3.triggered.connect(self.__presentador.mostrar_operacion_3)
        self.ac_op4.triggered.connect(self.__presentador.mostrar_operacion_4)
        self.ac_op5.triggered.connect(self.__presentador.mostrar_operacion_5)

    def closeEvent(self, e):
        res = QMessageBox.question(self, 'Salir!!', 'Seguro que desea salir?', QMessageBox.Yes | QMessageBox.No)
        if res == QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

    def mover_al_medio(self):
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho / 2) - (self.frameSize().width() / 2)
        top = (resolucion_alto / 2) - (self.frameSize().height() / 2)
        self.move(left, top)

    def resizeEvent(self, a0: QResizeEvent):
        background = QPixmap('vista/img/fondo.jpg')
        background = background.scaled(self.size(), Qt.IgnoreAspectRatio)
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(pal)

    def annadir_titulo(self):
        dias = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}
        meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
                 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
        dia_sem = dias[date.today().weekday()]
        dia = str(date.today().day)
        mes = meses[date.today().month]
        anno = str(date.today().year)
        msg = 'Sistema de bases de taxis. Fecha Actual: ({}  {} de {} del {})'.format(dia_sem, dia, mes, anno)
        self.setWindowTitle(msg)
