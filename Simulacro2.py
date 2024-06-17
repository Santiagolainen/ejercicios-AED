def fin_palabra(car_ant, car):
    if car_ant != ' ' and (car == ' ' or car == '.'):
        return True
    return False

def prom(n1, n2):
    if n2 != 0:
        return n1//n2

def main():
    m = open('entrada.txt', 'rt')
    texto = m.read()
    car_ant = None
    long_pal = cont_vocales = cont_consonantes = pal_par_consonante_vocales = pal_max_digito_p = cont_letras_s = cont_pal_s = cont_pal_vocal_ra = 0
    contiene_p = contiene_digito = contiene_s = contiene_ra = contiene_vocal = False
    vocales = 'aeiou'
    for car in texto:
        
        if car != ' ' and car != '.':
            
            long_pal += 1

            # Punto 1
            if car.lower() in vocales:
                cont_vocales += 1
            elif 'z' >= car.lower() >= 'a' and car.lower() not in vocales:
                cont_consonantes += 1
            
            # Punto 2
            if car.lower() == 'p':
                contiene_p = True

            if '9' >= car >= '0':
                contiene_digito = True
            
            # Punto 3
            if car.lower() == 's':
                contiene_s = True

            # Punto 4
            if car_ant is not None:
                if car_ant.lower() == 'r' and car.lower() == 'a':
                    contiene_ra = True

            if long_pal == 1 or long_pal == 2:
                if car.lower() in vocales:
                    contiene_vocal = True
        
        if fin_palabra(car_ant, car):
            if long_pal % 2 == 0:
                if cont_consonantes == cont_vocales:
                    pal_par_consonante_vocales += 1

            if not contiene_p and contiene_digito:
                if long_pal > pal_max_digito_p:
                    pal_max_digito_p = long_pal

            if contiene_s and long_pal > 2:
                cont_letras_s += long_pal
                cont_pal_s += 1

            if contiene_ra and contiene_vocal:
                cont_pal_vocal_ra += 1

            cont_consonantes = cont_vocales = long_pal = 0
            contiene_ra = contiene_vocal = contiene_p = contiene_digito = False
            

        car_ant = car
    
    promedio = prom(cont_letras_s, cont_pal_s)
    print(pal_par_consonante_vocales)
    print(pal_max_digito_p)
    print(promedio)
    print(cont_pal_vocal_ra)
    m.close()

if __name__ == '__main__':
    main()