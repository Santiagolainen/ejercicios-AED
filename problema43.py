def validate(inf):
    n = inf

    while n <= inf:
        n = int(input(f'Ingrese un número mayor a {inf}: '))
        if n <= inf:
            print(f'Error, debe ingresar un número mayor a {inf}')

    return n



def carga(n):
    v = []

    for i in range(n):
        v.append(int(input(f'Ingrese un número entero: ')))

    return v



def check(k, v):
    n = len(v)

    for i in range(n):
        if v[i] % k != 0:
            return False
    return True

def main():
    n = validate(0)
    v = carga(n)
    k = int(input('Ingrese una secuencia "k": '))

    es_secuencial = check(k, v)

    if es_secuencial:
        print(f'El arreglo esta ordenado en secuencia {k} en {k}')
    else:
        print(f'El arreglo no esta ordenado en secuencia {k} en {k}')


if __name__ == '__main__':
    main()