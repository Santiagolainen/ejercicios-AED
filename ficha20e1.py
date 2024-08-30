import random

class Atermico:
    def __init__(self, reg, m, tmax, tmin):
        self.region = reg
        self.mes = m
        self.tmaxima = tmax
        self.tminima = tmin

    def __str__(self):
        return (f'Región: {self.region} - Mes: {self.mes} - Temperatura máxima: {self.tmaxima}° - Temperatura '
                f'mínima: {self.tminima}°')

def validate(inf):
    n = inf

    while n <= inf:
        n = int(input(f'Ingrese un valor mayor a {inf}: '))
        if n <= inf:
            print(f'Error, se solicitó un valor mayor a {inf}')

    return n


def cargar_random(n):
    regiones = ('Norte', 'Sur', 'Este', 'Oeste')
    v_temp = []

    for i in range(n):
        reg = random.choice(regiones)
        m = random.randint(1, 12)
        tmax = random.randint(20, 40)
        tmin = random.randint(-10, 20)
        v_temp.append(Atermico(reg, m, tmax, tmin))

    return v_temp


def display(v):
    for i in range(len(v)):
        print(v[i])


def prom(suma, cant):
    if cant == 0:
        return

    return suma//cant


def search_min(v):
    minima = None
    region = ''
    mes = 0

    for i in range(len(v)):
        if minima is None or v[i].tminima < minima:
            minima = v[i].tminima
            region = v[i].region
            mes = v[i].mes

    return region, mes

def main():
    n = validate(0)

    op = -1

    while op != 4:
        print('Menu de opciones')
        print('='*120)
        print('1) Cargar análisis termicos')
        print('2) Mostrar temperatura máxima promedio en el primer semestre')
        print('3) Mostrar región y mes en el que se registró la menor mínima del año')
        print('4) Salir')
        op = int(input())

        if op == 1:
            v_temperaturas = cargar_random(n)
            display(v_temperaturas)
        elif op == 2:
            suma = cont = 0
            for i in range(len(v_temperaturas)):
                if v_temperaturas[i].mes <= 6:
                    suma += v_temperaturas[i].tmaxima
                    cont += 1
            promedio = prom(suma, cont)
            print(f'La temperatura máxima promedio en el primer semestre fue de {promedio}°')
        elif op == 3:
            region, mes = search_min(v_temperaturas)
            print(f'La menor temperatura mínima registrada se dió en la región {region} en el mes {mes}')


    print('Programa finalizado...')


if __name__ == '__main__':
    main()