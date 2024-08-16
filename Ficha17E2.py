import random

def porc(n1, n2):
    if n2 != 0:
        return n1*100//n2
    

def sum_impar(d1, d2):
    for i in range(len(d1)):
        if (d1[i] + d2[i]) % 2 != 0:
            return i + 1


def val_may(d):
    n = len(d)
    may = 0
    cont = 0

    for i in range(n):
        if d[i] > may:
            may = d[i]
            cont = 0
        if d[i] == may:
            cont += 1
    
    return may, cont
    

def sum(n, sums_posibles, d1, d2):
    sum = sums = 0
    for i in range(n):
        sum = d1[i] + d2[i]
        sums += sum
        sums_posibles[sum - 2] += 1
    return sums


def mostrar_sums(sums_posibles):
    n = len(sums_posibles)

    for i in range(n):
        if sums_posibles[i] != 0:
            print(f'Cantidad de veces que se sumo {i+2}: {sums_posibles[i]}')


def sums_may_prom(promedio, sums_posibles):
    cont = 0
    for i in range(len(sums_posibles)):
        if sums_posibles[i] != 0 and i + 2 > promedio:
            cont += sums_posibles[i]
    
    return cont

def main():
    d1 = []
    d2 = []
    sums_posibles = [0] * 11
    cmv = pos_sum_impar = may1 = may2 = cont_may1 = cont_may2 = 0
    n = int(input('Ingrese la cantidad de veces que desea que los dados se tiren: '))

    for i in range(n):
        n1 = random.randint(1, 6)
        n2 = random.randint(1,6)
        d1.append(n1)
        d2.append(n2)

        if n1 == n2:
            cmv += 1
    
    pos_sum_impar = sum_impar(d1, d2)
    porcentaje = porc(cmv, n)
    may1, cont_may1 = val_may(d1)
    may2, cont_may2 = val_may(d2)
    sums = sum(n, sums_posibles, d1, d2)
    promedio = sums//n
    cont_sum_may_prom = sums_may_prom(promedio, sums_posibles)


    print(f'La cantidad de veces que ámbos dados tuvieron el mismo valor fueron {cmv} veces, eso representa'
          f'un {porcentaje}% sobre el total de tiradas')
    if pos_sum_impar is None:
        print('No se dió una suma impar entre ambos dados')
    else:
        print(f'La primera vez que se dió una suma impar entre ambos dados fue en el lanzamiento {pos_sum_impar}')
    print(f'El valor máximo del primer dado fue de {may1}, este se repitió {cont_may1} veces')
    print(f'El valor máximo del segundo dado fue de {may2}, este se repitió {cont_may2} veces')
    mostrar_sums(sums_posibles)
    print(f'La cantidad de tiradas en las que la suma de ambos dados fue mayor que la suma promedio ({promedio}) de todas las tiradas fueron {cont_sum_may_prom} tiradas')
    print(d1)
    print(d2)

if __name__ == '__main__':
    main()