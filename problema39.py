def carga(n, v_nombres, v_edades, v_sueldos):

    for i in range(n):
        v_nombres[i] = input(f'Ingrese el nombre de la persona {i + 1}: ')
        v_edades[i] = int(input(f'Ingrese la edad de la persona {i + 1}: '))
        v_sueldos[i] = int(input(f'Ingrese el sueldo de la persona {i + 1}: '))


def sort(v_nombres, v_edades, v_sueldos):
    n = len(v_nombres)
    for i in range(n - 1):
        for j in range(i+1, n):
            if v_nombres[i] > v_nombres[j]:
                v_nombres[i], v_nombres[j] = v_nombres[j], v_nombres[i]
                v_edades[i], v_edades[j] = v_edades[j], v_edades[i]
                v_sueldos[i], v_sueldos[j] = v_sueldos[j], v_sueldos[i]


def mostrar(v_nombres, v_edades, v_sueldos):
    n = len(v_nombres)
    print('Personas que tienen más de 18 años y ganan menos de 10.000$')
    for i in range(n):
        if v_edades[i] > 18 and v_sueldos[i] < 10000:
            print(f'Nombre: {v_nombres[i]}')


def main():
    n = int(input('Ingrese la cantidad de personas: '))

    v_nombres = n * ['']
    v_edades = n * [0]
    v_sueldos = n * [0.0]

    carga(n, v_nombres, v_edades, v_sueldos)
    sort(v_nombres, v_edades, v_sueldos)
    mostrar(v_nombres, v_edades, v_sueldos)


if __name__ == '__main__':
    main()