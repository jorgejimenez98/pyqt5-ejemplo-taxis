from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QPalette, QPixmap, QBrush, QResizeEvent
from PyQt5.QtCore import Qt
from PyQt5 import uic


class Dialogo_1(QDialog):
    def __init__(self, presentador):
        QDialog.__init__(self)
        uic.loadUi('vista/ui/operacion_1.ui', self)
        self.__presentador = presentador
        self.setMaximumSize(447, 91)
        self.setMinimumSize(447, 91)

        self.btn_close.clicked.connect(self.close)
        self.btn_mostrar.clicked.connect(self.__presentador.fun_mostrar_informacion)

    def resizeEvent(self, a0: QResizeEvent):
        background = QPixmap('vista/img/fondo.jpg')
        background = background.scaled(self.size(), Qt.IgnoreAspectRatio)
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(pal)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error!!', msg)

    def mostrar_informacion(self, res, cod):
        msg = 'El importe del viaje ({}) es:\n $ ({}).'.format(cod, str(res))
        QMessageBox.information(self, 'Respuesta', msg)

    @property
    def valor_cod_viaje(self):
        return self.txt_codigo.text().strip()

    @valor_cod_viaje.setter
    def valor_cod_viaje(self, value):
        self.txt_codigo.setText(value)

    def validar_operacion(self):
        if len(self.valor_cod_viaje) == 0:
            raise Exception("El código de viaje no puede estar vacío")
        if len(self.valor_cod_viaje) != 5:
            raise Exception("El código de viaje debe tener obligatoriamente 5 caracteres")
