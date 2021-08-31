from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QDialog
from PyQt5.QtGui import QPixmap, QBrush, QResizeEvent, QPalette
from PyQt5.QtCore import Qt
from PyQt5 import uic


class Dialogo_5(QDialog):
    def __init__(self, presentador):
        QDialog.__init__(self)
        uic.loadUi('vista/ui/operacion_5.ui', self)
        self.__presentador = presentador

        self.annadir_eventos()
        self.annadir_elementos_tabla()
        self.tabla.resizeColumnsToContents()


    def annadir_eventos(self):
        self.btn_close.clicked.connect(self.close)
        self.btn_mostrar.clicked.connect(self.__presentador.fun_mostrar_informacion)

    def annadir_elementos_tabla(self):
        self.tabla.setColumnCount(10)
        self.tabla.setHorizontalHeaderLabels(
            ['C Viaje', 'Fecha inicio', 'Fecha termina', '# Taxi', 'Distancia Klm', 'CTHAC', 'Nombre C', 'Sexo C',
             'Edad C', 'Exp C'])
        self.tabla.horizontalHeaderItem(0).setToolTip('Código de viaje')
        self.tabla.horizontalHeaderItem(3).setToolTip('Número de Taxi')
        self.tabla.horizontalHeaderItem(4).setToolTip("Número de pasajeros")
        self.tabla.horizontalHeaderItem(5).setToolTip('Chofer tuvo que habilitar antes de su culminación?')
        self.tabla.horizontalHeaderItem(6).setToolTip('Pasó algún embotellamiento?')
        self.tabla.horizontalHeaderItem(6).setToolTip('Nombre del chofer')
        self.tabla.horizontalHeaderItem(7).setToolTip('Sexo del chofer')
        self.tabla.horizontalHeaderItem(8).setToolTip('Edad del chofer')
        self.tabla.horizontalHeaderItem(9).setToolTip('Experiencia del chofer')

    def resizeEvent(self, a0: QResizeEvent):
        background = QPixmap('vista/img/fondo.jpg')
        background = background.scaled(self.size(), Qt.IgnoreAspectRatio)
        pal = self.palette()
        pal.setBrush(QPalette.Background, QBrush(background))
        self.setPalette(pal)

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error!!', msg)

    def agregar_elemento_tabla(self, fil, col, text):
        self.tabla.setItem(fil, col, QTableWidgetItem(str(text)))

    def vaciar_tabla(self):
        while self.tabla.rowCount() > 0:
            self.tabla.removeRow(0)
