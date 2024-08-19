import random

def carga():
    n = int(input('Ingrese el número de la tarjeta (si ingresa -1 corta la carga): '))
    tarjetas = []
    while n != -1:
        if 9999999999999999 > n > 1000000000000000:
            tarjetas.append(n)
            n = int(input('Ingrese el número de la tarjeta (si ingresa -1 corta la carga): '))
        elif n != -1:
            print('Error, número no válido')
            n = int(input('Ingrese el número de la tarjeta (si ingresa -1 corta la carga): '))

    return tarjetas


def pagos_rechazados(v1, v2):
    m_rechazadas = [0] * 9
    for i in range(len(v1)):
        for j in range(len(v2)):
            if v1[i] == v2[j]:
                m_rechazadas[int(v1[i][0]) - 1] += 1

    return m_rechazadas



def may_pagos_rechazados(v, marcas):
    may = im = 0
    for i in range(len(v)):
        if v[i] > may:
            may = v[i]
            im = i

    return marcas[im]


def main():
    t_invalidas = carga()

    tarjetas = carga()

    marcas = ['Vasa', 'American Slow', 'MasterCard', 'Tarjeta Pomelo', 'Launcher\'s club', 'JNoCB', 'AsiaPay', 'Undiscovered Card', 'AED Card']
    m_rechazadas = pagos_rechazados(tarjetas, t_invalidas)

    for i in range(len(m_rechazadas)):
        print(f'Cantidad de tarjetas {marcas[i]} rechazadas: {m_rechazadas[i]}')

    mmpr = may_pagos_rechazados(m_rechazadas, marcas)
    print(f'\nLa marca con mayor cantidad de tarjetas rechazadas es {mmpr}')


if __name__ == '__main__':
    main()