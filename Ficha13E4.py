def es_vocal(car):
    car = car.lower()
    return car in 'aeiouáéíóú'


def es_consonante(car):
    car = car.lower()
    return car in 'bcdfghjklmnñpqrstvwxyz'


def porc(n1, n2):
    if n2 != 0:
        return int((n1*100)/n2)
    return 0


def main():
    texto = 'En este parcial estamos evaluando lógica.'

    cl = cpfv = cv = cct = clt = cp = cmc = cc = omc = cppt = 0
    car_ant = ' '
    tst = tppt = False
    pct = texto[0].lower()
    for car in texto:
        if car in ' .':
            cp += 1
            if es_vocal(car_ant):
                cpfv += 1

            if cc > cmc:
                cmc = cc
                omc = cp

            if tst and tppt:
                cppt += 1
            cc = cl = 0
            tst = tppt = False
        else:
            cl += 1
            clt += 1

            if es_vocal(car):
                cv += 1
            if es_consonante(car):
                cct += 1
                cc += 1

            if car_ant.lower() == 's' and car.lower() == 't':
                tst = True
            if cl == 1 and car.lower() == pct:
                tppt = True

        car_ant = car

    porv = porc(cv, clt)
    porcc = porc(cct, clt)

    print(f'La cantidad de palabras que finalizan en vocal son: {cpfv}')
    print(f'El porcentaje de vocales por sobre el total de caracteres en el texto es de {porv}% y de '
          f'consonantes es {porcc}%')
    print(f'La palabra con más consonantes tuvo {cmc} consonantes y esta en la posición {omc}')
    print(f'La cantidad de palabras que comenzaron con la primera letra de todo el texto e incluyen "st" son: {cppt}')


if __name__ == '__main__':
    main()