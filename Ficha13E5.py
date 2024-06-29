def es_digito(car):
    return '9' >= car >= '0'


def prom(n1, n2):
    if n2 != 0:
        return n1/n2
    return 0


def main():
    texto = input('Ingrese un texto finalizado por punto: ')

    while '.' not in texto:
        print('Texto no válido')
        texto = input()

    cl = cd = cp2d = cpla = clla = cpllv = 0
    ela = ell = tv = False
    car_ant = ' '
    for car in texto:
        if car in ' .':

            if cd >= 2:
                cp2d += 1

            if ela:
                clla += cl

            if tv and ell:
                cpllv += 1

            cd = cl = 0
            ela = tv = ell = False

        else:

            cl += 1
            if es_digito(car):
                cd += 1

            if cl == 2:
                if car_ant.lower() == 'l' and car.lower() == 'a':
                    cpla += 1
                    ela = True

                if car_ant.lower() == 'l' and car.lower() == 'l':
                    ell = True
            if car.lower() == 'v':
                tv = True

        car_ant = car

    prom_pla = prom(clla, cpla)

    print(f'La cantidad de palabras con al menos 2 digitos son {cp2d} palabras')
    print(f'La cantidad de palabras que empiezan con "la" fueron {cpla} palabras')
    print(f'El promedio de letras de las palabras que cumplieron con el punto anterior es de {prom_pla} letras '
          f'por palabra')
    print(f'La cantidad de palabras que empiezan con "ll" e incluyeron alguna "v" fueron {cpllv} palabras')


if __name__ == '__main__':
    main()