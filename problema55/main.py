import clase
import pickle
import os.path


def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))

        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')

    return n


def validate_range(inf, sup, msg):
    n = int(input(msg))

    while n < inf or n > sup:
        print(f'Error, se solicitó un número en el rango [{inf}-{sup}]')
    
    return n

def main():
    op = -1
    v = []
    fn = 'problema55/libros.dat'

    while op != 0:
        print('Menu de opciones')
        print('='*120)
        print('1) Crear arreglo')
        print('2) Mostrar arreglo')
        print('3) Crear archivo')
        print('4) Mostrar contenido del archivo')
        print('5) Crear archivo con datos de libro menor a x')
        print('6) Crear en memoria el arreglo v a partir del archivo')
        print('7) Crear en memoria el arreglo v a partir del archivo con datos mayores a x')
        print('0) Salir')
        op = int(input())
        print()

        if op == 1:
            n = validate(0, 'Ingrese la cantidad de libros que desea cargar en el arreglo: ')
            v = [None] * n
            clase.generate_random(v)
            print('Listo, arreglo cargado')
            print()
        elif op == 2:
            if v:
                clase.display(v)
            else:
                print('Error, el arreglo no ha sido cargado aún...')
                print()
        elif op == 3:
            if v:
                m = open(fn, 'wb')

                for lib in v:
                    pickle.dump(lib, m)
                m.close()

                print('Archivo creado con exito')
                print()
            else:
                print('Error, el arreglo no ha sido cargado aún...')
                print()
        elif op == 4:
            if v:
                if os.path.exists(fn):
                    print('Contenido del arhcivo')
                    t = os.path.getsize(fn)
                    m = open(fn, 'rb')
                    while m.tell() < t:
                        lib = pickle.load(m)
                        print(lib)
                    
                    m.close()
                    print()
                else:
                    print('Error, el archivo no ha sido creado aún...')
                    print()
            else:
                print('Error, el arreglo no ha sido cargado aún...')
                print()
        elif op == 5:
            if v:
                x = validate_range(100, 999, 'Ingrese el número de código mínimo que se desea almacenar en el nuevo archivo: ')
                m = open(fn, 'wb')
                for lib in v:
                    if lib.isbn < x:
                        pickle.dump(lib, m)
                m.close()
                print('Listo, archivo creado con exito')
                print()
            else:
                print('Error, el arreglo no ha sido cargado aún...')
                print()
        elif op == 6:
            if v:
                if os.path.exists(fn):
                    v = []
                    m = open(fn, 'rb')
                    t = os.path.getsize(fn)

                    while m.tell() < t:
                        v.append(pickle.load(m))
                    m.close()
                    print('Arreglo cargado correctamente')
                    print()
                else:
                    print('Error, el archvio aún no ha sido creado...')
                    print()
            else:
                print('Error, el arreglo no ha sido cargado aún...')
                print()
        elif op == 7:
            if v:
                x = validate_range(100, 999, 'Ingrese el valor x: ')
                m = open(fn, 'rb')
                t = os.path.getsize(fn)
                v = []

                while m.tell() < t:
                    lib = pickle.load(m)

                    if lib.isbn > x:
                        v.append(lib)
                
                print('Arreglo cargado con exito...')
                print()
            else:
                print('Error, el arreglo no ha sido cargado aún...')
                print()




if __name__ == '__main__':
    main()