from PyQt5.QtWidgets import QMessageBox, QDialog


class Dialogo_3(QDialog):
    def __init__(self, presenter):
        QDialog.__init__(self)
        self.__presenter = presenter

    def mostrar_error(self, msg):
        QMessageBox.critical(self, 'Error!!', msg)

    def mostrar_informacoion(self, msg):
        res = 'El porciento es del {} %'.format(str(msg))
        QMessageBox.information(self, 'Respuesta!!', res)

    def calculo(self):
        self.__presenter.fun_mostrar_informacion()
