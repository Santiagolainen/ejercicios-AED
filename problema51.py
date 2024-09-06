import random

def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))
        if n <= inf:
            print(f'Error, se solicitó un valor mayor a {inf}')
    
    return n


def crear_matriz(n, m):
    v = [0] * n

    for f in range(n):
        v[f] = [0] * m
    
    return v


def carga(v):
    for f in range(len(v)):
        for c in range(len(v[f])):
            #v[f][c] = int(input(f'Ingrese la cantidad de el artículo {c} del empleado {f}: '))
            v[f][c] = random.randint(0, 20)


def cant_tot_vend(v):
    cont = [0] * len(v)
    for f in range(len(v)):
        for c in range(len(v[f])):
            cont[f] += v[f][c]
    
    return cont


def cant_tot_art(v):
    filas = len(v)
    columnas = len(v[0])
    cont = [0] * columnas

    for c in range(columnas):
        for f in range(filas):
            cont[c] += v[f][c]
    
    return cont

def main():
    n = validate(0, 'Ingrese la cantidad de prodúctos: ')
    m = validate(0, 'Ingrese el número de vendedores: ')

    cant = crear_matriz(m, n)
    carga(cant)

    cont_vend = cant_tot_vend(cant)
    cont_art = cant_tot_art(cant)

    for i in range(len(cont_vend)):
        print(f'La cantidad total vendida por el vendedor {i} es de: {cont_vend[i]}')

    for i in range(len(cont_art)):
        print(f'La cantidad total vendida del artículo {i} es de: {cont_art[i]}')

    print(cant)


if __name__ == '__main__':
    main()