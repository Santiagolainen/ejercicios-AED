def array(vec):
    for i in range(len(vec)):
        vec[i] = int(input(f'Ingrese un número para la posicion {i+1}: '))
        while vec[i] < 0:
            print('Valor incorrecto, ingrese un número mayor a 0')
            vec[i] = int(input())

if __name__ == '__main__':
    array()