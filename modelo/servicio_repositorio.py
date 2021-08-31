from modelo.funciones_de_ayuda import *


class Servicio_Repositorio:
    def __init__(self, rep):
        self.__repositorio = rep

    def importe_x_codigo_viaje(self, cod):
        if len(self.__repositorio.lista_viajes) == 0:
            raise Exception("No hay viajes registrados")
        for i in self.__repositorio.lista_viajes:
            if i.es_cod_viaje(cod):
                return i.importe()
        raise Exception("No hay viajes registrados con el codigo ({})".format(cod))

    def prom_edad_chferes__viajes_locales_pas_embote_x_fecha(self, fecha):
        if len(self.__repositorio.lista_viajes_locales()) == 0:
            raise Exception("No hay viajes locales registrados")
        cont, suma, hay_x_fecha, hay_embot = 0, 0, False, False
        for i in self.__repositorio.lista_viajes_locales():
            bol = valor_booleano(solo_fecha(i.fecha_inicio), solo_fecha(i.fecha_termina), fecha)
            if bol:
                hay_x_fecha = True
                if i.paso_embotellamineto:
                    hay_embot = True
                    cont += 1
                    suma += i.chofer.edad
        if not hay_x_fecha:
            raise Exception("No hay viajes locales registrados en la fecha ({})".format(str(fecha)))
        elif not hay_embot:
            raise Exception("No hay viajes locales registrados que hayan pasado por enbotellamiento")
        return round(suma / cont, 2)

    def porciento_viajes_locales_q_hicieron_por_servicio_taxi(self):
        if len(self.__repositorio.lista_viajes_locales()) == 0:
            raise Exception("No hay viajes locales registrados")
        total, parte, existe = 0, 0, False
        for i in self.__repositorio.lista_viajes_locales():
            total += 1
            if i.fue_servicio_recorrida:
                existe = True
                parte += 1
        if not existe:
            raise Exception("No hay viajes locales registrados que hicieron el servicio se recorrida")
        return round((100 * parte) / total, 2)

    def datos_viaje_local_mayor_duracion_x_fecha(self, fecha):
        if len(self.__repositorio.lista_viajes_locales()) == 0:
            raise Exception("No hay viajes locales registrados")
        existe = False
        lista = []
        for i in range(len(self.__repositorio.lista_viajes_locales())):
            e = self.__repositorio.lista_viajes_locales()[i]
            if solo_fecha(e.fecha_inicio) <= fecha <= solo_fecha(e.fecha_termina):
                existe = True
                dur = duracion(e.fecha_inicio, e.fecha_termina)
                tupla = (dur, i, e)
                lista.append(tupla)
        if not existe:
            raise Exception("No hay viajes locales registrados en la fecha ({})".format(str(fecha)))
        lista.sort(), lista.reverse()
        i = lista[0][2]
        res = [i.cod_viaje, i.fecha_inicio, i.fecha_termina, i.num_taxi, i.chofer.nombre, i.chofer.sexo,
               i.chofer.edad, i.chofer.experiencia, i.cant_pasajaros, i.fue_servicio_recorrida,
               i.paso_embotellamineto]
        return res

    def listado_viajes_fuera_ciudad_ordenado_x_distancia(self):
        if len(self.__repositorio.lista_viajes_fuera_ciudad()) == 0:
            raise Exception("No hay viajes fuera de la ciudad registrados")
        l = [i for i in self.__repositorio.lista_viajes_fuera_ciudad() if i.es_si_chofer_habilito(False)]
        if len(l) == 0:
            raise Exception("No hay viajes fuera de la ciudad registrados que no tengan el coche habilitado")
        l.sort()
        res = [[i.cod_viaje, i.fecha_inicio, i.fecha_termina, i.num_taxi, i.chofer.nombre, i.chofer.sexo,
                i.chofer.edad, i.chofer.experiencia, i.distancia_klm, i.si_chofer_habilito] for i in l]
        return res
