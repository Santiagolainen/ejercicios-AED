import clase


def validate(inf):
    n = inf

    while n <= inf:
        n = float(input('Ingrese el monto x: '))

        if n <= inf:
            print(f'Error, se solicitó un valor mayor a {inf}')
            n = float(input('Ingrese el monto x: '))
    
    return n


def main():
    m = open('ficha23e2/alquileres.csv', 'rt')

    line = m.readline()
    line = m.readline()
    v = []

    op = -1

    while op != 0:
        print('1) Cargar arreglo')
        print('2) Trasladar a un archivo')
        print('3) Mostrar monto total recaudado')
        print('0) Salir')
        op = int(input())

        if op == 1:
            while line != '':
                

                line = line.strip()

                valores = line.split(',')

                if int(valores[2]) <= 9 and int(valores[2]) >= 0:
                    v.append(clase.Alquiler(valores[0], float(valores[1]), int(valores[2])))

                line = m.readline()
            m.close()
        elif op == 2:
            x = validate(0)
            m = open('ficha23e2/alquieres_mayores_x.csv', 'wt')

            for vec in v:
                if vec.monto > x:
                    m.write(f'{vec.dni}, {vec.monto}, {vec.tipocabana}\n')
            
            m.close()
        elif op == 3:
            mont_cab = [0] * 10
            m = open('ficha23e2/alquieres_mayores_x.csv', 'rt')
            line = m.readline()
            while line != '':

                line = line.strip()

                valores = line.split(',')

                mont_cab[int(valores[2])] += float(valores[1])
                line = m.readline()
            m.close()
            print('Montos acumulados por cada tipo de cabaña:')
            for i in range(len(mont_cab)):
                print(f'Cabaña {i}: {round(mont_cab[i],2)}$')
    print('Programa finalizado...')
    
    

    



if __name__ == '__main__':
    main()