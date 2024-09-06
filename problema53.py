def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))
        if n <= inf:
            print(f'Error, se solicitó un valor mayor a {inf}')
    
    return n


def carga(v):
    for f in range(len(v)):
        for c in range(len(v[f])):
            v[f][c] = int(input(f'Ingrese el valor para [{f}][{c}]: '))


def sum_tri_sup(v):
    suma = 0
    for f in range(len(v) - 1):
        for c in range(f+1 ,len(v[f])):
            suma += v[f][c]
    
    return suma

def suma_tri_inf(v):
    cp = 0
    for f in range(1, len(v)):
        for c in range(f):
            if v[f][c] % 2 == 0:
                cp += 1
    
    return cp


def el_0_diag(v):
    c0 = 0
    for f in range(len(v)):
        if v[f][f] == 0:
            c0 += 1
    
    return c0


def display(v):
    for f in range(len(v)):
        print(v[f])


def main():
    n = validate(0, 'Ingrese la dimensión de la matríz: ')
    
    mat = n * [0]
    for f in range(n):
        mat[f] = [0] * n
    
    carga(mat)

    suma_t_superior = sum_tri_sup(mat)
    cp = suma_tri_inf(mat)
    c0 = el_0_diag(mat)

    print()
    print(f'La suma del triángulo superior de la matríz es: {suma_t_superior}')
    print()
    print(f'La cantidad de números pares en el triángulo inferior de la matríz son: {cp}')
    print()
    print(f'La cantidad de 0 en la diagonal principal de la matríz son: {c0}')
    print()
    display(mat)


if __name__ == '__main__':
    main()