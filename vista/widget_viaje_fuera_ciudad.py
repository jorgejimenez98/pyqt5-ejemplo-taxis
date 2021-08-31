from modelo.funciones_de_ayuda import *
from PyQt5.QtWidgets import QMessageBox, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QBrush, QResizeEvent, QPalette
from PyQt5.QtCore import Qt
from PyQt5 import uic
from datetime import datetime


class Widget_Viaje_Fuera_Ciudad(QWidget):
    def __init__(self, presentador):
        QWidget.__init__(self)
        uic.loadUi('vista/ui/viaje_fuera_ciudad.ui', self)
        self.__presentador = presentador
        self.annadir_eventos()
        self.annadir_elementos_tabla()

    def annadir_eventos(self):
        self.btn_close.clicked.connect(self.close)
        self.btn_add.clicked.connect(self.__presentador.fun_add)
        self.btn_del.clicked.connect(self.__presentador.fun_del)
        self.btn_upt.clicked.connect(self.__presentador.fun_upt)
        self.tabla.itemClicked.connect(self.__presentador.fun_fill)

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

    @property
    def valor_cod_viaje(self):
        return self.txt_codigo.text().strip()

    @valor_cod_viaje.setter
    def valor_cod_viaje(self, value):
        self.txt_codigo.setText(value)

    @property
    def valor_fecha_inicio(self):
        x = self.date_fecha_inicio.text()
        fecha = fecha_a_partir_del_visual(x)
        return fecha

    @valor_fecha_inicio.setter
    def valor_fecha_inicio(self, value):
        self.date_fecha_inicio.setDateTime(value)

    @property
    def valor_fecha_termina(self):
        x = self.date_fecha_termina.text()
        fecha = fecha_a_partir_del_visual(x)
        return fecha

    @valor_fecha_termina.setter
    def valor_fecha_termina(self, value):
        self.date_fecha_termina.setDateTime(value)

    @property
    def valor_num_taxi(self):
        return self.spn_numero_taxi.value()

    @valor_num_taxi.setter
    def valor_num_taxi(self, value):
        self.spn_numero_taxi.setValue(value)

    @property
    def valor_distancia(self):
        return self.spn_distancia.value()

    @valor_distancia.setter
    def valor_distancia(self, value):
        self.spn_distancia.setValue(value)

    @property
    def valor_hailitar(self):
        if self.check_habilitar.isChecked():
            return 'Si'
        else:
            return 'No'

    @valor_hailitar.setter
    def valor_hailitar(self, value):
        if value == 'Si':
            self.check_habilitar.setChecked(True)
        else:
            self.check_habilitar.setChecked(False)

    @property
    def valor_nombre_chofer(self):
        return self.txt_nombre.text().strip()

    @valor_nombre_chofer.setter
    def valor_nombre_chofer(self, value):
        self.txt_nombre.setText(value)

    @property
    def valor_sexo(self):
        if self.rb_mas.isChecked():
            return 'M'
        else:
            return 'F'

    @valor_sexo.setter
    def valor_sexo(self, value):
        if value == 'M':
            self.rb_mas.setChecked(True)
        else:
            self.rb_fem.setChecked(True)

    @property
    def valor_edad(self):
        return self.spn_edad.value()

    @valor_edad.setter
    def valor_edad(self, value):
        self.spn_edad.setValue(value)

    @property
    def valor_experiencia(self):
        return self.spn_exp.value()

    @valor_experiencia.setter
    def valor_experiencia(self, value):
        self.spn_exp.setValue(value)

    def reestablecer_valores(self):
        self.valor_cod_viaje = ''
        self.valor_fecha_inicio = datetime(2018, 1, 1, 0, 0)
        self.valor_fecha_termina = datetime(2018, 1, 1, 0, 0)
        self.valor_num_taxi = 1
        self.valor_distancia = 0
        self.valor_hailitar = 'No'
        self.valor_nombre_chofer = ''
        self.valor_sexo = 'M'
        self.valor_edad = 18
        self.valor_experiencia = 1

    def validad_controles(self):
        if len(self.valor_cod_viaje) == 0:
            raise Exception("El código de viaje no puede estar vacío")
        if len(self.valor_cod_viaje) != 5:
            raise Exception("El código de viaje debe tener obligatoriamente 5 caracteres")
        if self.valor_fecha_inicio > self.valor_fecha_termina:
            raise Exception("La fecha de inicio no puede ser mayor que la fecha de terminación")
        if self.valor_distancia == 0:
            raise Exception("La distancia en klm no puede ser 0")
        if len(self.valor_nombre_chofer) == 0:
            raise Exception("El nombre del chofer no puede estar vacío")
        for i in self.valor_nombre_chofer:
            if i.isdigit():
                raise Exception("El nombre del chofer no puede tener números")
