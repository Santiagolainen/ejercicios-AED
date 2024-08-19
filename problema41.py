def validate(inf):
    n = inf
    while n <= inf:
        n = int(input(f'Ingrese un valor "n" mayor a {inf}: '))
        if n <= inf:
            print(f'Error, el valor debe ser mayor a {inf}')

    return n

def carga(n):
    alturas = []

    for i in range(n):
        alturas.append(int(input(f'Ingrese la altura (en cm) de la persona {i+1}: ')))

    return alturas


def average(alturas):
    cant = len(alturas)
    suma = 0

    for i in range(cant):
        suma += alturas[i]

    if cant > 0:
        return suma //cant
    return -1


def cont(alturas, prom):
    c1 = c2 = 0

    for i in range(len(alturas)):
        if alturas[i] > prom:
            c1 += 1
        else:
            c2 += 1

    return c1, c2



def main():
    n = validate(0)
    alturas = carga(n)

    promedio = average(alturas)
    c1, c2 = cont(alturas, promedio)

    print(f'La altura promedio del grupo es de {promedio} cm')
    print(f'Hay {c1} personas que superan la altura media del grupo, y hay {c2} personas que estan por debajo de la media')

if __name__ == '__main__':
    main()