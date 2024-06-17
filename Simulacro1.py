def inicio_palabra(car_ant, car):
    if (car_ant is None or car_ant == ' ') and car != ' ':
        return True
    return False

def fin_palabra(car_ant, car):
    if car_ant != ' ' and (car == ' ' or car == '.'):
        return True
    return False

def prom(n1, n2):
    if n2 != 0:
        return n1//n2
    return 0

def d_consonante(car_ant, car, vocales):
    if car_ant.lower() == 'd' and car in vocales:
        return True
    return False

def main():
    m = open('entrada.txt', 'rt')
    texto = m.read()
    car_ant = None
    primer_digito_impar = comienza_vocal = contiene_b = contiene_d_vocal = contiene_d_vocal_2 = False
    cars_mayus = no_contiene_m_a = True
    cont_pal_imp_min = long_palabras = long_max_pal_vocales_b = cont_consonantes = cont_vocales = cont_pal_mas_consonantes = cont_letras_mas_consonantes = cont_pal_d_vocal_2 = 0
    vocales = 'aeiou'

    for car in texto:

        if inicio_palabra(car_ant, car):
            if '9' >= car >= '0':
                if int(car) % 2 != 0:
                    primer_digito_impar = True
            if car.lower() in vocales:
                comienza_vocal = True
        
        if car not in ' .':
            long_palabras += 1
            if car.lower() == 'b':
                contiene_b = True
            if car.lower() == 'm' or car.lower() == 'a':
                no_contiene_m_a = False
            if car in vocales:
                cont_vocales += 1
            else:
                cont_consonantes += 1
            if car_ant is not None:
                if d_consonante(car_ant, car, vocales):
                    if contiene_d_vocal:
                        contiene_d_vocal_2 = True
                if d_consonante(car_ant, car, vocales):
                    contiene_d_vocal = True

        if primer_digito_impar:
            if 'Z' >= car >= 'A' or '0' >= car >= '9':
                cars_mayus = False

        if fin_palabra(car_ant, car):
            if cars_mayus:
                cont_pal_imp_min += 1
            if comienza_vocal and contiene_b:
                if long_palabras > long_max_pal_vocales_b:
                    long_max_pal_vocales_b = long_palabras
            if no_contiene_m_a:
                if cont_consonantes > cont_vocales:
                    cont_letras_mas_consonantes += long_palabras
                    cont_pal_mas_consonantes += 1
            if car_ant.lower() in vocales and contiene_d_vocal_2:
                cont_pal_d_vocal_2 += 1
            no_contiene_m_a = True
            long_palabras = cont_vocales = cont_consonantes = 0
            cars_mayus = contiene_b = primer_digito_impar = comienza_vocal = contiene_d_vocal = contiene_d_vocal_2 = False
        
    
        car_ant = car

    m.close()
    promedio = prom(cont_letras_mas_consonantes, cont_pal_mas_consonantes)
    print(cont_pal_imp_min)
    print(long_max_pal_vocales_b)
    print(promedio)
    print(cont_pal_d_vocal_2)

if __name__ == '__main__':
    main()