import clase

def search(v, x):
    for i in range(len(v)):
        if v[i].codigo == x:
            return True
    return False

def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))

        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')
            n = int(input(msg))
    
    return n


def validate_range(inf, sup, msg):
    n = int(input(msg))

    while n < inf or n > sup:
        print(f'Error, se solicitó un número en el rango [{inf}-{sup}]')
        n = int(input(msg))
    
    return n


def cont_mont(v):
    mat_p = [[]] * 6

    for f in range(len(mat_p)):
        mat_p[f] = [0] * 8
    
    for i in range(len(v)):
        mat_p[v[i].tiporesidencia][v[i].cantpersonas - 1] += v[i].monto
    
    return mat_p


def create_new(v, x):
    v_new = []

    for i in range(len(v)):
        if v[i].monto < x and 0 <= v[i].tiporesidencia < 4:
            v_new.append(v[i])
    
    return v_new


def sort(v):
    n = len(v)
    h = 1

    while h <= n//9:
        h = 3*h+1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y.codigo < v[k].codigo:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3


def det_mont(mat, res):
    suma = 0
    for c in range(len(mat[res])):
        suma += mat[res][c]

    return suma 

    

def main():
    op = -1
    fn = 'ficha24e2/alquileres.csv'
    v = clase.generate(fn)
    mat_p = []
    residencias = ('Departamento', 'Cabaña', 'Hotel Spa', 'Casa', 'Chalet', 'Hostería')

    while op != 6:
        print('Menu de opciones')
        print('='*120)
        print('1) Mostrar vector')
        print('2) Agregar nuevo alquiler')
        print('3) Determinar monto total')
        print('4) Crear nuevo arreglo')
        print('5) Mostrar monto total de un tipo de residencia')
        print('6) Salir')
        op = int(input())

        if op == 1:
            if v:
                clase.display(v)
            else:
                print('El archivo no existe')
            print()
        elif op == 2:
            if v:
                cod = input('Ingrese el número de reserva: ')
                existe = search(v, cod)

                if existe:
                    print('Ya existe esa reserva')
                else:
                    nom = input('Ingrese el nombre: ')
                    cantp = validate_range(1, 8, 'Ingrese la cantidad de personas: ')
                    tipor = validate_range(0, 5, 'Ingrese el tipo de residencia: ')
                    mont = float(input('Ingrese el monto a cobrar: '))
                    cantd = validate(0, 'Ingrese la cantidad de días: ')

                    v.append(clase.Reserva(cod, nom, cantp, tipor, mont, cantd))
            else:
                print('El archivo no existe')
            print()
        elif op == 3:
            if v:
                
                mat_p = cont_mont(v)
                
                for f in range(len(mat_p)):
                    for c in range(len(mat_p[f])):
                        if mat_p[f][c] != 0:
                            print(f'El monto de "{residencias[f]}" con {c+1} invitados fue de: {round(mat_p[f][c],2)}$')
            else:
                print('El archivo no existe')
            print()
        elif op == 4:
            if v:
                x = float(input('Ingrese el monto: '))

                v_new = create_new(v, x)
                sort(v_new)
                clase.display(v_new)
            else:
                print('El archivo no existe')
            print()
        elif op == 5:
            if v:
                if mat_p:
                    res = validate_range(0, 5, 'Ingrese el tipo de residencia: ')
                    suma = det_mont(mat_p, res)
                    print(f'Monto total a cobrar para la residencia "{residencias[res]}": {suma}$')
                else:
                    print('Error, la matríz no se ha cargado aún')

            else:
                print('El archivo no existe')
            print()
        elif op == 6:
            if v:
                m = open(fn, 'wt')
                m.write('numero,nombre,personas,tipo,monto,dias\n')
                for i in range(len(v)):
                    m.write(f'{v[i].codigo},{v[i].nombre},{v[i].cantpersonas},{v[i].tiporesidencia},{v[i].monto},{v[i].cantdias}\n')

                m.close()
    
    print('Programa finalizado...')


if __name__ == '__main__':
    main()