import os.path

import clase
import random
import pickle

def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))

        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')

            n = int(input(msg))

    return n


def add_in_order(v, articulo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].titulo == articulo.titulo:
            pos = c
            break

        if v[c].titulo < articulo.titulo:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq

    v[pos:pos] = [articulo]

def carga_arreglo(n, v):
    titulos = ('Leon el rey', 'Papa frita', 'Salame', 'Boludon', 'Gil', 'El salto del papu :v', 'Me lo robaron carmain',
               'Todo', 'Y eso era hoy', 'Hoy')

    for i in range(n):
        cod = random.randint(0, 999)
        tit = random.choice(titulos)
        cp = random.randint(0, 30)
        ta = random.randint(0, 9)
        idio = random.randint(0, 5)

        articulo = clase.Articulo(cod, tit, cp, ta, idio)
        add_in_order(v, articulo)


def display(v):
    for vec in v:
        print(vec)


def binary_search(v, x):
    n = len(v)
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].titulo == x:
            return c

        if v[c].titulo < x:
            izq = c + 1
        else:
            der = c - 1

    return -1


def busqueda_secuencial(v, x):
    for i in range(len(v)):
        if v[i].codigo == x:
            return i

    return -1


def generar_matriz(v):
    mat = [0] * 10

    for f in range(len(mat)):
        mat[f] = [0] * 6

    for i in range(len(v)):
        mat[v[i].tipoarticulo][v[i].idioma] += 1

    return mat


def crear_archivo(fn, v):
    m = open(fn, 'wb')
    for i in range(len(v)):
        if v[i].cantpag > 10:
            pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(fn):
    m = open(fn, 'rb')
    t = os.path.getsize(fn)
    while m.tell() < t:
        articulo = pickle.load(m)
        print(articulo)
    m.close()

def main():
    op = -1
    v = []
    fn = 'articulos10.dat'

    while op != 0:
        print('Menu de opciones')
        print('='*120)
        print('1) Cargar arreglo')
        print('2) Mostrar arreglo')
        print('3) Buscar artículo por título')
        print('4) Buscar artículo por código')
        print('5) Mostrar artículos por tipo e idioma')
        print('6) Generar archivo')
        print('7) Mostrar archivo')
        print('0) Salir')
        op = int(input())

        if op == 1:
            n = validate(0, 'Ingrese la cantidad de articulos que desea cargar: ')
            carga_arreglo(n, v)
            print()
        elif op == 2:
            if v:
                display(v)
            else:
                print('Error, el arreglo no ha sido cargado aún')
            print()
        elif op == 3:
            if v:
                titulo = input('Ingrese el título del artículo a buscar: ')
                pos = binary_search(v, titulo)

                if pos != -1:
                    print('Artículo encontrado')
                    print(v[pos])
                else:
                    print('Artículo no encontrado')
            else:
                print('Error, el arreglo no ha sido cargado aún')
            print()
        elif op == 4:
            if v:
                codigo = int(input('Ingrese el código del artículo a buscar: '))
                pos = busqueda_secuencial(v, codigo)

                if pos != -1:
                    print('Artículo encontrado')
                    print(v[pos])
                else:
                    print('Artículo no encontrado')
            else:
                print('Error, el arreglo no ha sido cargado aún')
            print()
        elif op == 5:
            if v:
                mat = generar_matriz(v)
                for f in range(len(mat)):
                    for c in range(len(mat[f])):
                        if mat[f][c] > 0:
                            print(f'La cantidad de artículos del tipo {f} en el idioma {c} son: {mat[f][c]}')
            else:
                print('Error, el arreglo no ha sido cargado aún')
            print()
        elif op == 6:
            if v:
                crear_archivo(fn, v)
                print('Archivo creado con éxito')
            else:
                print('Error, el arreglo no ha sido cargado aún')
            print()
        elif op == 7:
            if os.path.exists(fn):
                mostrar_archivo(fn)
            else:
                print('Error, el archivo no existe')
            print()

    print('Programa finalizado...')


if __name__ == '__main__':
    main()