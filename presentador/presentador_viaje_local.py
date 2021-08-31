from modelo.servicio_repositorio import Servicio_Repositorio
from modelo.funciones_de_ayuda import *
from modelo.viaje_local import Viaje_Local
from modelo.chofer import Chofer
from vista.widget_viaje_local import Widget_Viaje_Local


class Presentador_Viaje_Local:
    def __init__(self, rep):
        self.__repositorio = rep
        self.__servicio_repositorio = Servicio_Repositorio(self.__repositorio)

    def iniciar(self):
        self.__vista = Widget_Viaje_Local(self)
        self.cargar_datos()
        self.__vista.show()

    def validar_botones(self):
        if len(self.__repositorio.lista_viajes_locales()) == 0:
            self.__vista.btn_upt.setEnabled(False)
            self.__vista.btn_del.setEnabled(False)
        else:
            self.__vista.btn_upt.setEnabled(True)
            self.__vista.btn_del.setEnabled(True)

    def cargar_datos(self):
        self.validar_botones()
        self.__vista.vaciar_tabla()
        for i in self.__repositorio.lista_viajes_locales():
            x = self.__vista.tabla.rowCount()
            self.__vista.tabla.insertRow(x)
            fecha_inicio = fecha_en_cadena_a_partir_del_datetime(i.fecha_inicio)
            fecha_termina = fecha_en_cadena_a_partir_del_datetime(i.fecha_termina)
            servicio = 'No'
            if i.fue_servicio_recorrida:
                servicio = 'Si'
            llamada = 'No'
            if i.paso_embotellamineto:
                llamada = 'Si'
            self.__vista.agregar_elemento_tabla(x, 0, i.cod_viaje)
            self.__vista.agregar_elemento_tabla(x, 1, fecha_inicio)
            self.__vista.agregar_elemento_tabla(x, 2, fecha_termina)
            self.__vista.agregar_elemento_tabla(x, 3, i.num_taxi)
            self.__vista.agregar_elemento_tabla(x, 4, i.cant_pasajaros)
            self.__vista.agregar_elemento_tabla(x, 5, servicio)
            self.__vista.agregar_elemento_tabla(x, 6, llamada)
            self.__vista.agregar_elemento_tabla(x, 7, i.chofer.nombre)
            self.__vista.agregar_elemento_tabla(x, 8, i.chofer.sexo)
            self.__vista.agregar_elemento_tabla(x, 9, i.chofer.edad)
            self.__vista.agregar_elemento_tabla(x, 10, i.chofer.experiencia)
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
            cant_pas = int(self.__vista.tabla.item(ind, 4).text())
            servicio = self.__vista.tabla.item(ind, 5).text()
            emb = self.__vista.tabla.item(ind, 6).text()
            nombre = self.__vista.tabla.item(ind, 7).text()
            sexo = self.__vista.tabla.item(ind, 8).text()
            edad = int(self.__vista.tabla.item(ind, 9).text())
            exp = int(self.__vista.tabla.item(ind, 10).text())
            fecha_inicio = fecha_a_partir_del_visual(fecha_inicio1)
            fecha_termina = fecha_a_partir_del_visual(fecha_termina1)

            self.__vista.valor_cod_viaje = cod
            self.__vista.valor_fecha_inicio = fecha_inicio
            self.__vista.valor_fecha_termina = fecha_termina
            self.__vista.valor_num_taxi = num_tax
            self.__vista.valor_cant_pasajeros = cant_pas
            self.__vista.valor_llamada_servicio = servicio
            self.__vista.valor_pasa_embotlellamiento = emb
            self.__vista.valor_nombre_chofer = nombre
            self.__vista.valor_sexo = sexo
            self.__vista.valor_edad = edad
            self.__vista.valor_experiencia = exp

    def objeto_a_partir_tabla(self, ind):
        cod = self.__vista.tabla.item(ind, 0).text()
        fecha_inicio1 = self.__vista.tabla.item(ind, 1).text()
        fecha_termina1 = self.__vista.tabla.item(ind, 2).text()
        num_tax = int(self.__vista.tabla.item(ind, 3).text())
        cant_pas = int(self.__vista.tabla.item(ind, 4).text())
        servicio = self.__vista.tabla.item(ind, 5).text()
        emb = self.__vista.tabla.item(ind, 6).text()
        nombre = self.__vista.tabla.item(ind, 7).text()
        sexo = self.__vista.tabla.item(ind, 8).text()
        edad = int(self.__vista.tabla.item(ind, 9).text())
        exp = int(self.__vista.tabla.item(ind, 10).text())
        fecha_inicio = fecha_a_partir_del_visual(fecha_inicio1)
        fecha_termina = fecha_a_partir_del_visual(fecha_termina1)
        serv = False
        if servicio == 'Si':
            serv = True
        embo = False
        if emb == 'Si':
            embo = True
        c = Chofer(nombre, sexo, edad, exp)
        obj = Viaje_Local(cod, fecha_inicio, fecha_termina, num_tax, c, cant_pas, serv, embo)
        return obj

    def objeto_a_partir_del_visual(self):
        cod = self.__vista.valor_cod_viaje
        fecha_inicio = self.__vista.valor_fecha_inicio
        fecha_termina = self.__vista.valor_fecha_termina
        num_taxi = self.__vista.valor_num_taxi
        cant_pas = self.__vista.valor_cant_pasajeros:
        servicio = self.__vista.valor_llamada_servicio
        serv = False
        if servicio == 'Si':
            serv = True
        emobtella = self.__vista.valor_pasa_embotlellamiento
        emb = False
        if emobtella == 'Si':
            emb = True
        nombre = self.__vista.valor_nombre_chofer
        sexo = self.__vista.valor_sexo
        edad = self.__vista.valor_edad
        exp = self.__vista.valor_experiencia
        chofer = Chofer(nombre, sexo, edad, exp)
        viaje = Viaje_Local(cod, fecha_inicio, fecha_termina, num_taxi, chofer, cant_pas, serv, emb)
        return viaje
