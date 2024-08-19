def cargar(v, viaje):
    b = []

    for i in range(len(v)):
        b.append(int(input(f'Cantidad de pasajeros de {viaje} en la {v[i]}: ')))

    return b



def total_pasajeros(v):
    suma = 0

    for i in range(len(v)):
        suma += v[i]

    return suma



def max_pasajeros(estaciones, v_ida):
    may = im = 0

    for i in range(len(v_ida)):
        if v_ida[i] > may:
            may = v_ida[i]
            im = i

    return estaciones[im]



def no_pasajeros(v):
    cant = 0
    for i in range(len(v)):
        if v[i] == 0:
            cant += 1

    if cant != 0:
        return cant, (cant*100)//len(v)



def mas_ida_vuelta(v1, v2, estaciones):
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            print(f'{estaciones[i]}')


def main():
    estaciones = ['Maipú', 'Borges', 'Libertador', 'Anchorena', 'Barrancas', 'San Isidro R', 'Punta Chica',
                  'Marina Nueva', 'San Fernando R', 'Canal', 'Delta']

    v_ida = cargar(estaciones, 'ida')
    v_vuelta = cargar(estaciones, 'vuelta')
    op = -1
    while op != 6:
        print('Menu de opciones')
        print('='*80)
        print('1 - Mostrar datos cargados\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t 2 - Mostrar pasajeros en total que '
              'subieron en la ida y pasajeros que se '
              'subieron en la vuelta')
        print('3 - Mostrar estación en la se subieron mayor cantidad de pasajeros durante el viaje de ida\t\t\t\t\t\t 4 - Mostrar '
              'estaciones en las que no subieron pasajeros y el porcentaje que representan')
        print('5 - Mostrar estaciones en las que la cantidad de pasajeros del viaje de ida fue mayor a la del viaje'
              'de vuelta\t 6 - Salir')
        op = int(input())

        if op == 1:
            print(f'Estaciones: {estaciones}')
            print(f'Pasajeros en la ida: {v_ida}')
            print(f'Pasajeros en la vuelta: {v_vuelta}')
        elif op == 2:
            tpi = total_pasajeros(v_ida)
            tpv = total_pasajeros(v_vuelta)
            print(f'La cantidad de pasajeros que se subieron en la ida fueron {tpi} pasajeros')
            print(f'La cantidad de pasajeros que se subieron en la vuelta fueron {tpv} pasajeros')
        elif op == 3:
            empi = max_pasajeros(estaciones, v_ida)
            print(f'La estación con mayor cantidad de pasajeros en la ida fue la estación {empi}')
        elif op == 4:
            cesp, porcsp = no_pasajeros(v_vuelta)
            print(f'La cantidad de estaciones en la vuelta en las que no se subió ningún pasajero fueron {cesp} '
                  f'estaciones')
            print(f'Eso representa un {porcsp}% sobre el total de estaciones')
        elif op == 5:
            print('Las estaciones en las que se subieron más pasajeros en la ida que en la vuelta fueron las estaciones: ')
            mas_ida_vuelta(v_ida, v_vuelta, estaciones)
        else:
            print('Opción no válida')

    print('Programa finalizado... pipi pupu')

if __name__ == '__main__':
    main()