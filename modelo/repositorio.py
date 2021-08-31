from modelo.viaje_local import Viaje_Local
from modelo.viaje_fuera_ciudad import Viaje_Fuera_Ciudad


class Repositorio:
    def __init__(self):
        self.__lista_viajes = []

    @property
    def lista_viajes(self):
        return self.__lista_viajes

    def lista_viajes_locales(self):
        l = [i for i in self.lista_viajes if isinstance(i, Viaje_Local)]
        return l

    def lista_viajes_fuera_ciudad(self):
        l = [i for i in self.lista_viajes if isinstance(i, Viaje_Fuera_Ciudad)]
        return l

    def ind_viaje_x_cod(self, cod):
        for i in range(len(self.lista_viajes)):
            if self.lista_viajes[i].cod_viaje == cod:
                return i
        return -1

    def eliminar_viaje_x_codigo(self, cod):
        ind = self.ind_viaje_x_cod(cod)
        if ind == None:
            raise Exception("No existe el viaje")
        del self.lista_viajes[ind]

    def actualizar_viaje(self, obj_viejo, obj_nuevo):
        ind_ant = self.ind_viaje_x_cod(obj_viejo.cod_viaje)
        ind_new = self.ind_viaje_x_cod(obj_nuevo.cod_viaje)
        if ind_ant == -1:
            raise Exception('No existe ese viaje')
        if ind_new != None and ind_new != ind_ant:
            raise Exception("Ya existe ese viaje")
        self.lista_viajes[ind_ant] = obj_nuevo

    def insertar_viaje(self, o):
        existe_cod = False
        existe_taxi = False
        for i in self.lista_viajes:
            if i.cod_viaje == o.cod_viaje:
                existe_cod = True
            elif i.num_taxi == o.num_taxi:
                existe_taxi = True
        if existe_cod:
            raise Exception("Ya existe un viaje con el código de viaje ({})".format(o.cod_viaje))
        elif existe_taxi:
            raise Exception("Ya existe un taxi de número ({})".format(str(o.num_taxi)))
        self.lista_viajes.append(o)
