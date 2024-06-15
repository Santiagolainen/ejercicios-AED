__author__ = 'Santiago'

def get_text():
    texto = input('Ingrese un texto finalizado por un punto: ')
    
    while '.' not in texto:
        print('Texto invalido')
        texto = input()
    
    return texto

def prom(n1, n2):
    if n2 != 0:
        return n1/n2
    
def final_palabra(car_ant, car):
    if car_ant != ' ' and (car == ' ' or car == '.'):
        return True
    return False

def inicio_palabra(car_ant, car):
    if (car_ant is None or car_ant == ' ') and car != ' ':
        return True
    return False

def menu():
    print('Menu de opciones:')
    print('Elija una opción\n')
    print('1 - Promedio general de letras por palabra del texto')
    print('2 - Cantidad de palabras terminadas en vocal.')
    print('3 - Orden de la palabra más larga del texto.')
    print('4 - Cantidad de palabras que contengan al menos una vez la sílaba l+vocal (es decir la, le, li, lo o lu).')
    print('5 - Cantidad de palabras que incluyan algún dígito en la primera mitad.')
    print('6 - Salir')
    op = int(input())

    return op

def main():

    print('Palabras con expresión "l+vocal"')
    print('='*80)
    texto = get_text()
    
    cont_pal_digitos = letras_palabras = posicion_digito = cont_letras = cont_palabras = cont_pal_fin_vocal = long_pal = pal_max = orden_pal_max = cont_pal_lvocal = 0
    car_ant = None
    pal_digito = pal_lvocal = False
    vocales = 'aeiou'
    for car in texto:
    
        if car != ' ' and car != '.':
            cont_letras += 1
            long_pal += 1
            letras_palabras += 1
        
        if '9' >= car >= '0' and not pal_digito:
            pal_digito = True
            posicion_digito = letras_palabras

        if inicio_palabra(car_ant, car):
            cont_palabras += 1
        
        if car_ant is not None:
            if final_palabra(car_ant, car):
                if car_ant in vocales:
                    cont_pal_fin_vocal += 1

                if long_pal > pal_max:
                    orden_pal_max = cont_palabras
                    pal_max = long_pal

                if pal_digito:
                    if letras_palabras / 2 > posicion_digito:
                        cont_pal_digitos += 1

                pal_lvocal = False
                letras_palabras = 0
                pal_digito = False

            if car_ant.lower() == 'l' and car in vocales and not pal_lvocal:
                cont_pal_lvocal += 1
                pal_lvocal = True
        
        if car == '.':
            break

        car_ant = car
    
    promedio = prom(cont_letras,cont_palabras)

    op = menu()

    while op != 6:
        if op == 1:
            print(f'\nEl promedio general de letras por palabra del texto es de {promedio} letras por palabra\n\n')
            op = menu()
        elif op == 2:
            print(f'\nLa cantidad de palabras terminadas en vocal son {cont_pal_fin_vocal} palabras\n\n')
            op = menu()
        elif op == 3:
            print(f'\nEl orden de la palabra más larga del texto es {orden_pal_max}\n\n')
            op = menu()
        elif op == 4:
            print(f'\nLa cantidad de palabras que contienen al menos una vez la silaba "l+vocal" son {cont_pal_lvocal} palabras\n\n')
            op = menu()
        elif op == 5:
            print(f'\nLa cantidad de palabras que incluyen algún dígito en la primera mitad son {cont_pal_digitos} palabras\n\n')
            op = menu()
        else:
            print('\nComando no válido\n\n')
            op = menu()
    print('\nFinalizando programa...')



if __name__ == '__main__':
    main()