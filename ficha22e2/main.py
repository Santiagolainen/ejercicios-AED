import clase

def prom(n1, n2):
    
    if n2 != 0:
        return round(n1/n2,2)
    
    return 0


def shell_sort(v):
    n = len(v)
    h = 1

    while h < n // 9:
        h = 3*h + 1
    
    while h > 0:
        
        for j in range(h, n):
            y = v[j]
            k = j - h

            while k >= 0 and y.promedio > v[k].promedio:
                v[k + h] = v[k]
                k -= h
            v[k + h] = y
        
        h //= 3


def main():
    n = int(input('Ingrese la cantidad de alumnos a cargar: '))
    v = [None] * n

    clase.generate_random(v)
    shell_sort(v)
    clase.display(v)
    suma = 0

    for vec in v:
        suma += vec.promedio
    
    promedio = prom(suma, len(v))

    print('3 Alumnos con mejor promedio de la materia')

    for i in range(3):
        print(f'{i+1}) Nombre: {v[i].nombre} - Promedio: {v[i].promedio}')
    
    print(f'El promedio general de la materia fué: {promedio}')


if __name__ == '__main__':
    main()