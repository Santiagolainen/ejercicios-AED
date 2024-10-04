import clase
import pickle
import os
import io

def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))

        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')

            n = int(input(msg))

    return n

def buscar(m, fn, dni):
    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)
    t = os.path.getsize(fn)

    pos = -1

    while m.tell() < t:
        votante = pickle.load(m)
        fp = m.tell()

        if votante.dni == dni:
            pos = fp
            break

    m.seek(fp_inicial, io.SEEK_SET)

    return pos


def agregar_archivo(fn):
    m = open(fn, 'a+b')

    cod = validate(-1, 'Ingrese el número de documento del votante (si ingresa 0 se cancela la carga): ')
    while cod != 0:
        existe = buscar(m, fn, cod)

        if existe == -1:
            nom = input('Ingrese el nombre: ')
            ed = validate(15, 'Ingrese la edad del votante: ')
            sex = input('Ingrese el sexo (v:varon; m:mujer): ')
            votante = clase.Votante(cod, nom, ed, sex)
            pickle.dump(votante, m)
            m.flush()
        else:
            print('Error, esa persona ya está en el padrón')

        cod = validate(-1, 'Ingrese el número de documento del votante (si ingresa 0 se cancela la carga): ')


    m.close()


def mostrar_archivo(fn):
    t = os.path.getsize(fn)
    m = open(fn, 'rb')

    while m.tell() < t:
        votante = pickle.load(m)

        print(f'Votante {votante}')


def votantes_v_m(fn):
    t = os.path.getsize(fn)
    m = open(fn, 'rb')
    v = mu = 0

    while m.tell() < t:
        votante = pickle.load(m)

        if votante.sexo == 'v':
            v += 1
        else:
            mu += 1

    m.close()

    return v, mu


def generar_nuevo_archivo(fn, fn2):
    m = open(fn, 'rb')
    s = open(fn2, 'wb')
    t = os.path.getsize(fn)

    while m.tell() < t:
        votante = pickle.load(m)

        if votante.edad > 70:
            pickle.dump(votante, s)

    s.close()
    m.close()



def main():
    op = -1
    fn = 'votantes.dat'
    fn2 = 'votantes70.dat'

    while op != 0:
        print('Menu de opciones')
        print('='*120)
        print('1) Cargar archivo')
        print('2) Mostrar datos del archivo')
        print('3) Buscar votante por DNI')
        print('4) Mostrar votantes vaores y mujeres')
        print('5) Generar nuevo archivo')
        print('6) Mostrar archvio nuevo')
        print('0) Salir')
        op = int(input())

        if op == 1:
            agregar_archivo(fn)
            print('Archivo creado correctamente')
            print()
        elif op == 2:
            if os.path.exists(fn):
                mostrar_archivo(fn)
            else:
                print('El archivo no existe')
            print()
        elif op == 3:
            if os.path.exists(fn):
                x = validate(0, 'Ingrese el DNI a buscar: ')
                print()
                m = open(fn, 'rb')
                pos = buscar(m, fn, x)

                if pos != -1:
                    print('Votante encontrado')
                    m.seek(pos, io.SEEK_SET)
                    votante = pickle.load(m)
                    print(votante)
                else:
                    print('Vontante no encontrado')
                m.close()
            else:
                print('El archvio no existe')
            print()
        elif op == 4:
            if os.path.exists(fn):
                var, muj = votantes_v_m(fn)
                print(f'Hay {var} votantes hombres')
                print(f'Hay {muj} votantes mujeres')
            else:
                print('El archivo no existe')
        elif op == 5:
            if os.path.exists(fn):
                generar_nuevo_archivo(fn, fn2)
            else:
                print('El archivo no existe')
            print()
        elif op == 6:
            if os.path.exists(fn2):
                mostrar_archivo(fn2)
            else:
                print('El archivo no existe')

    print('Programa finalizado')


if __name__ == '__main__':
    main()