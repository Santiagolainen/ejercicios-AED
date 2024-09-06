def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))
        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')
    
    return n


def validate_range(a, b, msg=''):
    n = int(input(msg))

    while n < a or n > b:
        print(f'Error, se solicita un valor en el rango {a}-{b}')
        n = int(input(msg))
    
    return n


def carga(v, n):
    for i in range(n):
        f = validate_range(0, 4, f'Ingrese el destino de viaje del cliente {i}: ')
        c = validate_range(0, 2, f'Ingrese el metodo de pago del cliente {i}: ')
        v[f][c] += 1


def display(v):

    for f in range(len(v)):
        print()
        print(f'Destino {f}')
        for c in range(len(v[f])):
            print(f'Metodo de pago {c}: {v[f][c]}')

def main():
    n = validate(0, 'Ingrese la cantidad de clientes que desea cargar: ')

    mat = [0] * 5
    for f in range(5):
        mat[f] = [0] * 3
    
    carga(mat, n)
    
    display(mat)


if __name__ == '__main__':
    main()