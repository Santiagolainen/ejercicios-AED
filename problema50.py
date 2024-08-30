import random
from sys import flags

class Vehiculos:
    def __init__(self, pat, tv, nc, imp):
        self.patente = pat
        self.tipovehiculo = tv
        self.numcabina = nc
        self.importe = imp

    def __str__(self):
        return (f'Patente: {self.patente} - Tipo de vehículo: {self.tipovehiculo} - Número de cabina: {self.numcabina} - '
                f'Importe: {self.importe}')


def validate(inf):
    n = inf

    while n <= inf:
        n = int(input())
        if n <= inf:
            print(f'Error, se solicita un valor mayor a {inf}')
            n = int(input())

    return n


def validate_nc():
    nc = int(input('Ingrese el número de cabina (0 a 14): '))
    while nc > 14 or nc < 0:
        print('Error, ingrese un número de cabina dentro del rango(0 a 14): ')
        nc = int(input())

    return nc


def carga_random(n):
    letras = ('ABC', 'BCD', 'DEF', 'FGH')

    v_vehiculos = []

    for i in range(n):
        pat1 = random.choice(letras)
        pat2 = str(random.randint(100, 999))
        pat3 = random.choice(letras)
        pat = pat1 + pat2 + pat3

        tv = random.randint(1, 100)
        nc = random.randint(0, 14)
        imp = random.randint(0, 2000)
        v_vehiculos.append(Vehiculos(pat, tv, nc, imp))

    return v_vehiculos


def carga(n):
    v_vehiculos = []

    for i in range(n):
        pat = input('Ingrese la patente: ')
        tv = int(input('Ingrese el tipo de vehículo: '))
        nc = validate_nc()
        imp = float(input('Ingrese el importe pagado: '))
        v_vehiculos.append(Vehiculos(pat, tv, nc, imp))

    return v_vehiculos


def display(v):
    for i in range(len(v)):
        print(v[i])


def sort(v):
    n = len(v)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].patente > v[j].patente:
                v[i], v[j] = v[j], v[i]


def search_vx(v, x):
    print(f'Los vehículos que pasaron por la cabina {x} sin pagar fueron: ')
    for i in range(len(v)):
        if v[i].numcabina == x and v[i].importe == 0:
            print(v[i])

def cant_v_c(v):
    cant_v = [0] * 15
    cant_imp_v = [0] * 15

    for cabina in v:
        d = cabina.numcabina
        imp = cabina.importe
        cant_v[d] += 1
        cant_imp_v[d] += imp

    return cant_v, cant_imp_v


def pat_p(v, p):
    cont = 0
    for i in range(len(v)):
        if v[i].patente == p:
            cont += 1
            print(v[i])
    if cont > 0:
        print(f'La patente aparece un total de {cont} veces')
    else:
        print('La patente no pasó por el peaje')


def main():
    print('Ingrese la cantidad de vehículos:')
    n = validate(0)

    op = -1

    while op != 0:
        print()
        print('Menu de opciones')
        print('='*160)
        print('1) Cargar los vehículos')
        print('2) Generar en forma automatica los contenidos de cada registro')
        print('3) Mostrar todos los datos ordenados por patente de menor a mayor')
        print('4) Mostrar todos los datos de los vehículos que hayan pasado sin pagar por una cabina ingresada por teclado')
        print('5) Mostrar importe acumulado por cada cabina y mostrar la cantidad de vehículos que pasan por cada cabina')
        print('6) Determinar cuantas veces una patente ingresada por teclado fue registrada')
        print('0) Salir')
        op = int(input())
        if op == 1:
            v_vehiculos = carga(n)
            display(v_vehiculos)
        elif op == 2:
            v_vehiculos = carga_random(n)
            display(v_vehiculos)
        elif op == 3:
            sort(v_vehiculos)
            display(v_vehiculos)
        elif op == 4:
            x = validate_nc()
            search_vx(v_vehiculos, x)
        elif op == 5:
            cant_v, v_imp_c = cant_v_c(v_vehiculos)
            print('Información sobre cabinas')
            for i in range(15):
                print()
                print(f'Cabina {i}')
                print(f'Cantidad de vehículos que pasaron: {cant_v[i]}')
                print(f'Importe total acumulado: {v_imp_c[i]}')
        elif op == 6:
            p = input('Ingrese una patente a buscar: ')
            pat_p(v_vehiculos, p)

    print('Programa finalizado...')


if __name__ == '__main__':
    main()