from mesonbuild.scripts.python_info import paths

import Paciente
import random
import pickle
import os

def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))

        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')

    return n

def add_in_order(v, paciente):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].codigo == paciente.codigo:
            pos = c
            break

        if paciente.codigo < v[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [paciente]


def generate_random(n, v):
    nombres = ('Raul', 'Rabozzi', 'Pablo', 'Jorge', 'Enrique', 'Mariano', 'Florentina', 'Josefina')
    for i in range(n):
        cod = random.randint(0, 999)
        nom = f'{random.choice(nombres)} {i}'
        fech = random.randint(0, 30)
        code = random.randint(0, 9)

        paciente = Paciente.Paciente(cod, nom, fech, code)

        add_in_order(v, paciente)


def display(v):
    for vec in v:
        print(vec)


def pacientes_d(d, v):
    print(f'Pacientes que se atendieron hace {d} días: ')

    for paciente in v:
        if paciente.fecha >= d:
            print(paciente)


def binary_search(x, v):
    n = len(v)

    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].codigo == x:
            return c

        if v[c].codigo < x:
            izq = c + 1
        else:
            der = c - 1

    return -1

def crear_archivo(fn, v):
    m = open(fn, 'wb')

    for i in range(len(v)):
        pickle.dump(v[i], m)
    m.close()

def mostrar_archivo(fn):
    m = open(fn, 'rb')
    t = os.path.getsize(fn)

    while m.tell() < t:
        paciente = pickle.load(m)
        print(paciente)


def crear_nuevo_arr(fn, v_new):

    m = open(fn, 'rb')
    t = os.path.getsize(fn)

    while m.tell() < t:
        paciente = pickle.load(m)

        if paciente.codigoenfermedad >= 8:
            v_new.append(paciente)
    m.close()



def main():
    op = -1
    v = []
    v_new = []
    fn = 'pacientes.dat'

    while op != 0:
        print('Menu de opciones')
        print('='*120)
        print('1) Cargar arreglo')
        print('2) Mostrar datos pacientes día "d"')
        print('3) Buscar paciente')
        print('4) Mostrar datos del arreglo')
        print('5) Grabar datos del arreglo en un archivo')
        print('6) Mostrar archivo')
        print('7) Crear nuevo arreglo')
        print('8) Mostrar arreglo nuevo')
        print('0) Salir')
        op = int(input())
        print()

        if op == 1:
            n = validate(0, 'Ingrese la cantidad de pacientes que desea cargar: ')
            generate_random(n, v)
            print('Arreglo cargado correctamente')
            print()
        elif op == 2:
            if v:
                d = validate(-1, 'Ingrese la cantidad de días: ')
                pacientes_d(d, v)
            else:
                print('Error, el arreglo no se ha cargado aún')
            print()
        elif op == 3:
            if v:
                x = validate(0, 'Ingrese el n° de historia clínica a buscar: ')
                pos = binary_search(x, v)

                if pos != -1:
                    print('Paciente encontrado')
                    print(v[pos])
                else:
                    print('Paciente no encontrado')

            else:
                print('Error, el arreglo no se ha cargado aún')
            print()
        elif op == 4:
            if v:
                display(v)
            else:
                print('Error, el arreglo no se ha cargado aún')
            print()
        elif op == 5:
            if v:
                crear_archivo(fn, v)
                print('Archivo creado correctamente')
            else:
                print('Error, el arreglo no se ha cargado aún')
            print()
        elif op == 6:
            if os.path.exists(fn):
                print(f'Pacientes en el archivo "{fn}"')
                mostrar_archivo(fn)
            else:
                print('Error, el archivo no ha sido creado aún')
            print()
        elif op == 7:
            if os.path.exists(fn):
                crear_nuevo_arr(fn, v_new)
                print('Arreglo creado')
            else:
                print('Error, el arreglo no se ha cargado aún')
            print()
        elif op == 8:
            if v_new:
                display(v_new)
            else:
                print('Error, el arreglo no se ha cargado aún')
            print()

    print('Programa finalizado...')


if __name__ == '__main__':
    main()