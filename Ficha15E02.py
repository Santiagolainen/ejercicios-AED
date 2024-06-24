def read(v):
    n = len(v)
    for i in range(n):
        v[i] = int(input('Ingrese un número: '))


def veces_ultimo_digito(ud, v):
    cud = 0
    for i in range(len(v)):
        if v[i] == ud:
            cud += 1
    return cud - 1


def elementos_menores_primero(pd, v):
    nuevo_v = []
    for i in range(len(v)):
        if v[i] < pd and i != 0:
            nuevo_v.append(v[i])

    return nuevo_v


def main():
    n = int(input('Ingrese la cantidad de elementos del vector: '))

    v = n*[0]

    read(v)

    ud = v[-1]
    pd = v[0]

    cvud = veces_ultimo_digito(ud, v)
    vvmpv = elementos_menores_primero(pd, v)

    print(f'La cantidad de veces que se repite el último dígito son {cvud} veces')
    print(f'El vector nuevo generado sólo con los elementos menores al primer valor ingresado es {vvmpv}')


if __name__ == '__main__':
    main()