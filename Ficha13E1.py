def ini_palabra(car_ant, car):
    if (car_ant == ' ' or car_ant is None) and car != ' ':
        return True
    else:
        return False

def pal_SI(inicio_palabra, car_ant, car):
    if inicio_palabra:
        if car_ant == 'S' and car == 'I':
            return 1
    return 0

def pal_vocal_impar(car_ant, cont_letras, vocales):
    if cont_letras % 2 != 0:
        if car_ant in vocales:
            return 1
    return 0

def pal_igual_fin_in(car_inicial, car_ant):
    if car_inicial == car_ant.lower():
        return 1
    return 0

def porc(n1, n2):
    porcentaje = n1*100//n2
    return porcentaje

def prom(n1, n2):
    promedio = 0
    if n2 != 0:
        promedio = n1//n2
    return promedio

def main():
    texto = input('Ingrese un texto finalizado con un punto: ')
    car_ant = pal_corta = None
    inicio_palabra = True
    vocales = 'aeiouAEIOU'
    cont_pal_SI = cont_letras = cont_pal_vocales = cont_pal_una_vocal = cont_pal_in_fin = cont_pal_CC = cont_palabras = cont_letras_total = 0 
    pal_vocal = pal_vocal_definitivo = exp_CC = False
    car_inicial = ''

    while '.' not in texto:
        print('Ingrese un texto válido')
        texto = input()
    
    for car in texto:
        
        if car == ' ' or car == '.':
            if cont_letras % 2 != 0:
                cont_pal_vocales += pal_vocal_impar(car_ant, cont_letras, vocales)
            if pal_vocal_definitivo:
                cont_pal_una_vocal += 1
            if exp_CC == True:
                cont_pal_CC += 1
                exp_CC = False
            if pal_corta is None or cont_letras < pal_corta:
                pal_corta = cont_letras
            cont_pal_in_fin += pal_igual_fin_in(car_inicial, car_ant)
            cont_palabras += 1
            cont_letras = 0
            pal_vocal_definitivo = False
            pal_vocal = False
        else:
            if car_ant == 'C' and car == 'C':
                exp_CC = True
            cont_letras += 1
            cont_letras_total += 1

        if car in vocales and not pal_vocal:
            pal_vocal_definitivo = True
        elif car in vocales and pal_vocal:
            pal_vocal_definitivo = False

        if car in vocales:
            pal_vocal = True
        
        
        if car == '.':
            break

        cont_pal_SI += pal_SI(inicio_palabra, car_ant, car)

        inicio_palabra = ini_palabra(car_ant, car)

        if inicio_palabra:
            car_inicial = car.lower()
        
        
        car_ant = car

    porcentaje = porc(cont_pal_vocales, cont_palabras)
    promedio = prom(cont_letras_total, cont_palabras)
    print(f'La cantidad de palabras que comienzan con la expresion "SI" son {cont_pal_SI} palabras')
    print(f'La cantidad de palabras que terminan con vocal y tienen una cantidad impar de letras son {cont_pal_vocales} palabras')
    print(f'La cantidad de palabras que tienen sólo una vocal son {cont_pal_una_vocal} palabras')
    print(f'La cantidad de palabras que comienzan y terminan con la misma letra son {cont_pal_in_fin} palabras')
    print(f'La cantidad de palabras que contienen la expresion "CC" son {cont_pal_CC} palabras')
    print(f'El porcentaje que representa la cantidad de palabras que terminan con vocal y tienen una cantidad impar de letras es de un {porcentaje}%')
    print(f'La longitud de la palabra más corta es de {pal_corta} palabras')
    print(f'El promedio de letras por palabra es de {promedio} letras por palabra')

if __name__ == '__main__':
    main()
        
        