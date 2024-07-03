import arreglo


def main():
    n = int(input('Ingrese la cantidad de alumnos de los que desea ver el legajo: '))
    while n < 0:
        print('Cantidad no válida')
        n = int(input())
    
    legajos = arreglo.array(n)

    print(f'Los legajos son: {legajos}')

    arreglo.ord_men_may(legajos)
    print(f'Los legajos ordenados de menor a mayor son: {legajos}')

    x = int(input('Ingrese el legajo del alumno que desea encontrar: '))

    pos = arreglo.binary_search(legajos, x)

    if pos == -1:
        print('Error... Alumno no encontrado')
    else:
        print(f'Es el alumno número {pos}')

if __name__ == '__main__':
    main()
    