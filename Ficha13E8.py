def es_digito(car):
    return '9' >= car >= '0'


def prom(n1, n2):
    if n2 != 0:
        return n1/n2
    return 0

def main():
    texto = input('Ingrese un texto finalizado por un punto: ')

    cl = cld = cpd = pfdl = ppmc = cp = cpch = 0
    tl = tch = False
    pmc = None
    car_ant = ' '

    for car in texto:
        if car in ' .':
            cp += 1
            if not tl:
                cld += cl
                cpd += 1
            
            if tl and es_digito(car_ant):
                pfdl += 1
            
            if pmc is None or cl < pmc:
                ppmc = cp
                pmc = cl
            
            if tch:
                cpch += 1
                
            tl = tch = False
            cl = 0
        else:

            cl += 1

            if not es_digito(car):
                tl = True
            
            if cl >= 5 and car_ant.lower() == 'c' and car.lower() == 'h':
                tch = True

        car_ant = car
    
    promedio_dpp = prom(cld, cpd)
    
    print('Resultado 1:', promedio_dpp)
    print('Resultado 2:', pfdl)
    print(f'La longitud es {pmc} y el orden es {ppmc}')
    print('La cantidad de palabras que tienen las letras "ch" a partir de la cuarta letra son:', cpch)


if __name__ == '__main__':
    main()