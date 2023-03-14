def divisor():
    return print("------------------------------------------------------------")


def welcome():
    print("Bienvenido")
    print(""" Menu
    1. Mostrar Top 10 de canciones por artista
    0. Salir
    """)


def segundos_a_segundos_minutos_y_horas(ms):
    millis = int(ms)
    seconds = (millis / 1000) % 60
    seconds = int(seconds)
    minutes = (millis / (1000 * 60)) % 60
    minutes = int(minutes)
    hours = (millis / (1000 * 60 * 60)) % 24

    return str("%d:%d:%d" % (hours, minutes, seconds))
