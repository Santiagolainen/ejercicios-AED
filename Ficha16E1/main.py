import arreglo

def main():
    n = int(input('Ingrese la cantidad de elementos que tendrá el arreglo: '))
    while n < 0:
        print('Número no válido, inserte un número mayor a 0')
        n = int(input())

    vec = arreglo.array(n)
    print(f'El vector original es {vec}')

    arreglo.ord_asc(vec)
    
    print(f'Arreglo ordenado de forma ascendente: {vec}')

    x = int(input('Ingrese el elemento que desea encontrar en el arreglo: '))

    pos = arreglo.binary_search(vec, x)
    
    if pos == -1:
        print('No se encuentra el elemento en la lista')
    else:
        print(f'El elemento se encuentra en la posición {pos} de el arreglo')

if __name__ == '__main__':
    main()