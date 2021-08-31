from modelo.funciones_de_ayuda import fecha_a_partir_del_date
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QPalette, QPixmap, QBrush, QResizeEvent
from PyQt5.QtCore import Qt
from PyQt5 import uic


class Dialogo_2(QDialog):
    def __init__(self, presentador):
        QDialog.__init__(self)
        uic.loadUi('vista/ui/operacion_2.ui', self)
        self.__presentador = presentador
        self.setMaximumSize(432, 104)
        self.setMinimumSize(432, 104)

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

    def mostrar_informacion(self, res):
        msg = 'El promedio de edades los choferes es:\n({}).'.format(res)
        QMessageBox.information(self, 'Respuesta', msg)

    @property
    def valor_fecha(self):
        x = self.date_fecha.text()
        res = fecha_a_partir_del_date(x)
        return res

    @valor_fecha.setter
    def valor_fecha(self, value):
        self.date_fecha.setDate(value)
