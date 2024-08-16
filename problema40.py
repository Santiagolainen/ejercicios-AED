def carga(v):
    print('Ingrese números entre el 0 y el 99 (si ingresa -1 se corta):')
    n = int(input())
    while n != -1:
        if 99 >= n >= 0:
            v[n] += 1
            n = int(input())
        else:
            print('Ingrese un número válido')
            n = int(input())


def mostrar(v):
    n = len(v)

    for i in range(n):
        if v[i] != 0:
            print(f'Cantidad de {i}: {v[i]}')

def main():
    v = [0] * 100
    carga(v)
    mostrar(v)

if __name__ == '__main__':
    main()