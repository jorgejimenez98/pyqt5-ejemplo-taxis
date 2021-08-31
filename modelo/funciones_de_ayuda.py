from datetime import *


def valor_booleano(fecha_inicio, fecha_termina, fecha):
    return fecha_inicio <= fecha <= fecha_termina


def duracion(fecha_inicio, fecha_termina):
    f1 = solo_fecha(fecha_inicio)
    f2 = solo_fecha(fecha_termina)
    if f1 == f2:
        resta = resta_fecha(fecha_inicio, fecha_termina)[0]
        x = solo_hora(resta)
        resp = duracion_min(x)
    else:
        dias = int(resta_fecha(fecha_inicio, fecha_termina)[0])
        x = solo_hora(resta_fecha(fecha_inicio, fecha_termina)[2])
        dur = dias * 24 * 60
        resp = int(duracion_min(x)) + dur
    return resp


def duracion_min(x):
    h1, m1 = x[0] * 60, x[1]
    res = h1 + m1
    return res


def solo_hora(h):
    x = h.split(":")
    w, m = int(x[0]), int(x[1])
    res = [w, m]
    return res


def solo_fecha(f):
    x = date(f.year, f.month, f.day)
    return x


def resta_fecha(f1, f2):
    x = f2 - f1
    return str(x).split()


def valor_booleano_2(h):
    return time(7, 0) <= h <= time(19, 0)


def hora_a_partir_fecha(f):
    x = str(f).split()
    w = x[1].split(":")
    z, m = int(w[0]), int(w[1])
    res = time(z, m)
    return res


def fecha_a_partir_del_visual(fecha):
    f = fecha.split()
    f1, f2 = f[0].split("/"), f[1].split(":")
    d, m, a = int(f1[0]), int(f1[1]), int(f1[2])
    h, mi = int(f2[0]), int(f2[1])
    res = datetime(a, m, d, h, mi)
    return res


def fecha_en_cadena_a_partir_del_datetime(fecha):
    f = str(fecha).split()
    f1, f2 = f[0].split("-"), f[1].split(":")
    d, m, a = f1[2], f1[1], f1[0]
    h, mi = f2[0], f2[1]
    res = '{}/{}/{} {}:{}'.format(d, m, a, h, mi)
    return res


def fecha_a_partir_del_date(fecha):
    f = str(fecha).split("/")
    d, m, a = int(f[0]), int(f[1]), int(f[2])
    res = date(a, m, d)
    return res


def cadena_fecha(fecha):
    meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
             9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    dia = fecha.day
    mes = meses[fecha.month]
    anno = fecha.year
    res = '{} de {} del {}'.format(dia, mes, anno)
    return res
