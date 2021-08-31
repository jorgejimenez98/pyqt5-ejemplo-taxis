from modelo.viaje_fuera_ciudad import Viaje_Fuera_Ciudad
from modelo.chofer import Chofer
from modelo.servicio_repositorio import Servicio_Repositorio
from vista.widget_viaje_fuera_ciudad import Widget_Viaje_Fuera_Ciudad
from modelo.funciones_de_ayuda import *


class Presentador_Viaje_Fuera_Ciudad:
    def __init__(self, rep):
        self.__repositorio = rep
        self.__servicio_repositorio = Servicio_Repositorio(self.__repositorio)

    def iniciar(self):
        self.__vista = Widget_Viaje_Fuera_Ciudad(self)
        self.cargar_datos()
        self.__vista.show()

    def validar_botones(self):
        if len(self.__repositorio.lista_viajes_fuera_ciudad()) == 0:
            self.__vista.btn_upt.setEnabled(False)
            self.__vista.btn_del.setEnabled(False)
        else:
            self.__vista.btn_upt.setEnabled(True)
            self.__vista.btn_del.setEnabled(True)

    def cargar_datos(self):
        self.validar_botones()
        self.__vista.vaciar_tabla()
        for i in self.__repositorio.lista_viajes_fuera_ciudad():
            x = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(x)
            fecha_inicio = fecha_en_cadena_a_partir_del_datetime(i.fecha_inicio)
            fecha_termina = fecha_en_cadena_a_partir_del_datetime(i.fecha_termina)
            hab = 'No'
            if i.si_chofer_habilito:
                hab = 'Si'
            self.__vista.agregar_elemento_tabla(x, 0, i.cod_viaje)
            self.__vista.agregar_elemento_tabla(x, 1, fecha_inicio)
            self.__vista.agregar_elemento_tabla(x, 2, fecha_termina)
            self.__vista.agregar_elemento_tabla(x, 3, i.num_taxi)
            self.__vista.agregar_elemento_tabla(x, 4, i.distancia_klm)
            self.__vista.agregar_elemento_tabla(x, 5, hab)
            self.__vista.agregar_elemento_tabla(x, 6, i.chofer.nombre)
            self.__vista.agregar_elemento_tabla(x, 7, i.chofer.sexo)
            self.__vista.agregar_elemento_tabla(x, 8, i.chofer.edad)
            self.__vista.agregar_elemento_tabla(x, 9, i.chofer.experiencia)
        self.__vista.tabla.resizeColumnsToContents()

    def fun_add(self):
        try:
            self.__vista.validad_controles()
            viaje = self.objeto_a_partir_del_visual()
            self.__repositorio.insertar_viaje(viaje)
            self.cargar_datos()
            self.__vista.reestablecer_valores()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def fun_del(self):
        try:
            ind = self.__vista.tabla.currentRow()
            if ind == -1:
                raise Exception("Debes seleccionar una fila para eliminar")
            cod = self.__vista.tabla.item(ind, 0).text()
            self.__repositorio.eliminar_viaje_x_codigo(cod)
            self.cargar_datos()
            self.__vista.reestablecer_valores()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def fun_upt(self):
        try:
            ind = self.__vista.tabla.currentRow()
            if ind == -1:
                raise Exception("Debes seleccionar una fila para actualizar")
            self.__vista.validad_controles()
            obj_viejo = self.objeto_a_partir_tabla(ind)
            obj_nuevo = self.objeto_a_partir_del_visual()
            self.__repositorio.actualizar_viaje(obj_viejo, obj_nuevo)
            self.cargar_datos()
            self.__vista.reestablecer_valores()
        except Exception as e:
            self.__vista.mostrar_error(e.args[0])

    def fun_fill(self):
        ind = self.__vista.tabla.currentRow()
        if ind != -1:
            cod = self.__vista.tabla.item(ind, 0).text()
            fecha_inicio1 = self.__vista.tabla.item(ind, 1).text()
            fecha_termina1 = self.__vista.tabla.item(ind, 2).text()
            num_tax = int(self.__vista.tabla.item(ind, 3).text())
            dist = int(self.__vista.tabla.item(ind, 4).text())
            habilita = self.__vista.tabla.item(ind, 5).text()
            nombre = self.__vista.tabla.item(ind, 6).text()
            sexo = self.__vista.tabla.item(ind, 7).text()
            edad = int(self.__vista.tabla.item(ind, 8).text())
            exp = int(self.__vista.tabla.item(ind, 9).text())
            fecha_inicio = fecha_a_partir_del_visual(fecha_inicio1)
            fecha_termina = fecha_a_partir_del_visual(fecha_termina1)

            self.__vista.valor_cod_viaje = cod
            self.__vista.valor_fecha_inicio = fecha_inicio
            self.__vista.valor_fecha_termina = fecha_termina
            self.__vista.valor_num_taxi = num_tax
            self.__vista.valor_distancia = dist
            self.__vista.valor_hailitar = habilita
            self.__vista.valor_nombre_chofer = nombre
            self.__vista.valor_sexo = sexo
            self.__vista.valor_edad = edad
            self.__vista.valor_experiencia = exp

    def objeto_a_partir_del_visual(self):
        cod = self.__vista.valor_cod_viaje
        fecha_inicio = self.__vista.valor_fecha_inicio
        fecha_termina = self.__vista.valor_fecha_termina
        num_taxi = self.__vista.valor_num_taxi
        distancia = self.__vista.valor_distancia
        habilita = self.__vista.valor_hailitar
        hab = False
        if habilita == 'Si':
            hab = True
        nombre = self.__vista.valor_nombre_chofer
        sexo = self.__vista.valor_sexo
        edad = self.__vista.valor_edad
        exp = self.__vista.valor_experiencia
        chofer = Chofer(nombre, sexo, edad, exp)
        viaje = Viaje_Fuera_Ciudad(cod, fecha_inicio, fecha_termina, num_taxi, chofer, distancia, hab)
        return viaje

    def objeto_a_partir_tabla(self, ind):
        cod = self.__vista.tabla.item(ind, 0).text()
        fecha_inicio1 = self.__vista.tabla.item(ind, 1).text()
        fecha_termina1 = self.__vista.tabla.item(ind, 2).text()
        num_tax = int(self.__vista.tabla.item(ind, 3).text())
        dist = int(self.__vista.tabla.item(ind, 4).text())
        habilita = self.__vista.tabla.item(ind, 5).text()
        hab = False
        if habilita == 'Si':
            hab = True
        nombre = self.__vista.tabla.item(ind, 6).text()
        sexo = self.__vista.tabla.item(ind, 7).text()
        edad = int(self.__vista.tabla.item(ind, 8).text())
        exp = int(self.__vista.tabla.item(ind, 9).text())
        fecha_inicio = fecha_a_partir_del_visual(fecha_inicio1)
        fecha_termina = fecha_a_partir_del_visual(fecha_termina1)

        c = Chofer(nombre, sexo, edad, exp)
        obj = Viaje_Fuera_Ciudad(cod, fecha_inicio, fecha_termina, num_tax, c, dist, hab)
        return obj
