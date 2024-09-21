import random
import pickle
import os.path


def validate_range(inf, sup, msg):
    n = int(input(msg))

    while n < inf or n > sup:
        print(f'Error, se solicitó un número en el rango [{inf}-[{sup}]]')
        n = int(input())
    
    return n


def shell_sort(v):
    n = len(v)
    h = 1

    while h <= n//9:
        h = 3*h + 1
    
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h

            while k >= 0 and y < v[k]:
                v[k+h] = v[k]
                k -= h
            
            v[k+h] = y
        
        h //= 3


def display(v):
    for vec in v:
        print(vec)


def main():
    v = [0] * 6

    op = -1

    while op != 0:
        print('1) Cargar sorteo')
        print('2) Consultar')
        print('0) Salir')
        op = int(input())
        print()

        if op == 1:
            for i in range(6):
                v[i] = random.randint(0, 36)
            
            shell_sort(v)

            m = open('ficha23e1/extracto.dat', 'wb')

            for num in v:
                pickle.dump(num, m)
            
            m.close()
            print('Archivo cargado correctamente')
            print()
        elif op == 2:
            if os.path.exists('ficha23e1/extracto.dat'):
                t = os.path.getsize('ficha23e1/extracto.dat')
                m = open('ficha23e1/extracto.dat', 'rb')

                while m.tell() < t:
                    num = pickle.load(m)
                    print(f'Número: {num}')
                
                m.close()
                print()
            else:
                print('Error, el archivo no existe')
                print()
    

if __name__ == '__main__':
    main()