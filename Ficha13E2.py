__author__ = 'Santiago'

def prom(n1, n2):
    if n2 != 0:
        return n1/n2

def main():
    texto = input('Ingrese un texto terminado con un punto: ')

    while '.' not in texto:
        print('Texto inválido')
        texto = input()
    
    car_ant = None
    cont_pal_may = cont_nums = cont_pal_e = cont_e_pal = cont_pal = cont_letras = long_pal = 0

    for car in texto:
        if (car_ant is None or car_ant == ' ') and 'Z' >= car >= 'A':
            cont_pal_may += 1
        
        if car != ' ' and car != '.':
            cont_letras += 1
        
        if '9' >= car >= '0':
            cont_nums += 1
        
        if car.lower() == 'e':
            cont_e_pal += 1
        
        if car == ' ' or car == '.':
            if cont_e_pal >= 2:
                cont_pal_e += 1
            cont_e_pal = 0
            if cont_letras % 2 != 0:
                long_pal += cont_letras
                cont_pal += 1
            cont_letras = 0
        
        if car == '.':
            break

        car_ant = car
    
    promedio = prom(long_pal, cont_pal)
    
    print(f'Palabras que empiezan con mayúscula: {cont_pal_may}')
    print(f'Numeros del 0 al 9 en todo el texto: {cont_nums}')
    print(f'Palabras que tienen más de una e: {cont_pal_e}')
    print(f'Promedio de letras por palabra, para palabras de longitud impar: {promedio}')


if __name__ == '__main__':
    main()