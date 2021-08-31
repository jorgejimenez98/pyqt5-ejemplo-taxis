from modelo.funciones_de_ayuda import *
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QPalette, QPixmap, QBrush, QResizeEvent
from PyQt5.QtCore import Qt
from PyQt5 import uic


class Dialogo_4(QDialog):
    def __init__(self, presentador):
        QDialog.__init__(self)
        uic.loadUi('vista/ui/operacion_2.ui', self)
        self.__presentador = presentador
        self.setMaximumSize(432, 104)
        self.setMinimumSize(432, 104)
        self.setWindowTitle('Operación 4')

        self.btn_close.clicked.connect(self.close)
        self.btn_mostrar.clicked.connect(self.__presentador.fun_mostrar_informacion)
        self.btn_mostrar.setText('Calcular')

    def resizeEvent(self, a0: QResizeEvent):
        background = QPixmap('vista/img/fondo.jpg')
        background = background.scaled(self.size(), Qt.IgnoreAspectRatio)
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(pal)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error!!', msg)

    def mostrar_informacion(self, fecha, codigo, fecha_inicio, fecha_termina, num_taxi, nombre_chofer, llamada, embo):
        fec = cadena_fecha(fecha)
        fecha_1 = fecha_en_cadena_a_partir_del_datetime(fecha_inicio)
        fehca_2 = fecha_en_cadena_a_partir_del_datetime(fecha_termina)
        msg = 'Datos del viaje local de mayor duración de la fecha ({}):\n Código de viaje: {}\n Fecha de inicio: {}\n' \
              ' Fecha de terminación: {}\n Número de taxi: {}\n Nombre del chofer: {}\n Fue llamada de servicio: {}\n' \
              ' Pasó por embotellamiento: {}'.format(fec, codigo, fecha_1, fehca_2, str(num_taxi), nombre_chofer,
                                                     llamada, embo)
        QMessageBox.information(self, 'Respuesta', msg)

    @property
    def valor_fecha(self):
        x = self.date_fecha.text()
        res = fecha_a_partir_del_date(x)
        return res

    @valor_fecha.setter
    def valor_fecha(self, value):
        self.date_fecha.setDate(value)
