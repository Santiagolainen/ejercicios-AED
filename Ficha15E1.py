def prom(n1, n2):
    if n2 != 0:
        return int(n1 / n2)


def llpt(lista, fin, inicio=0):
    suma = 0
    for i in range(inicio, fin):
        suma += lista[i]
    return suma


def mes_mas_seco(lista):
    mmseco = None
    vmmseco = None
    for i in range(len(lista)):
        if vmmseco is None or lista[i] < vmmseco:
            vmmseco = lista[i]
            mmseco = i + 1

    return mmseco


def meses_mas_promedio(lista, promedio):
    meses = []

    for i in range(len(lista)):
        if lista[i] > promedio:
            meses.append(i + 1)

    return meses


def menu():
    print('Pluviómetro')
    print('='*80)
    print('Eliga una opción')
    print('1 - Determinar el promedio anual de lluvias\t 2 - Determinar el promedio de luvvias para un determinado '
          'trimestre')
    print('3 - Determinar el mes más seco del año     \t 4 - Determinar los meses del año en los que llovió más que el '
          'promedio de lluvia de todo el año')
    print('5 - Salir')
    op = int(input())
    return op


def main():

    preci = []

    for i in range(12):
        x = int(input(f'Ingrese la precipitación del mes {i+1}: '))
        preci.append(x)

    ap = 0
    for i in preci:
        ap += i
    pall = prom(ap, len(preci))
    op = menu()

    while op != 5:
        if op == 1:
            print(f'El promedio anual de lluvias es de {pall}')
            print('')
            op = menu()
        elif op == 2:
            trimestre = int(input('Ingrese el trimestre que desea calcular: '))
            at = 0
            if trimestre == 1:
                at = llpt(preci, 3)
            elif trimestre == 2:
                at = llpt(preci, 6, 3)
            elif trimestre == 3:
                at = llpt(preci, 9, 6)
            elif trimestre == 4:
                at = llpt(preci, 12, 9)
            else:
                print('Trimestre no válido')

            pllt = prom(at, 3)

            print(f'El promedio de lluvias para el trimestre {trimestre} es de: {pllt}')
            print('')
            op = menu()
        elif op == 3:
            mmseco = mes_mas_seco(preci)
            print(f'El mes más seco del año fue el mes {mmseco}')
            print('')
            op = menu()

        elif op == 4:
            mmllp = meses_mas_promedio(preci, pall)
            print(f'Los meses del año que llovieron más que el promedio de lluvia de todo el año '
                  f'fueron los meses: {mmllp}')
            print('')
            op = menu()
        else:
            print('Opcion no válida')
            print('')
            op = menu()
    print('Saliendo del programa pee pee poo poo...')


if __name__ == '__main__':
    main()
