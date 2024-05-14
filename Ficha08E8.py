__author__ = "Santiago"

import random

random.seed(95)
segundo_num = None
cont_nums_menores_segundo = 0
cont_nums_mult_6 = 0
cont_nums_mult_9 = 0
cont_nums_mult_6_9 = 0
max_num_mult_4 = 0

for i in range(45000):
    n = random.randint(1, 95000)

    if i == 1:
        segundo_num = n

    if i > 1 and n < segundo_num:
        cont_nums_menores_segundo += 1

    if n % 6 == 0:
        cont_nums_mult_6 += 1
    if n % 9 == 0:
        cont_nums_mult_9 += 1
    if n % 9 == 0 and n % 6 == 0:
        cont_nums_mult_6_9 += 1

    if n % 4 == 0 and n > max_num_mult_4:
        max_num_mult_4 = n

print(f"La cantidad de números que son menores al segundo número leído de la serie son {cont_nums_menores_segundo} números")
print(f"La cantidad de números que son múltiplos de 6 son {cont_nums_mult_6} números")
print(f"La cantidad de números que son múltiplos de 9 son {cont_nums_mult_9} números")
print(f"La cantidad de números que son múltiplos de 6 y 9 son {cont_nums_mult_6_9} números")
print(f"El mayor número múltiplo de 4 en la serie es el {max_num_mult_4}")
print(f"El porcentaje que representa la cantidad del punto 1 respecto del total de números procesados es de un {round((cont_nums_menores_segundo*100)/45000,2)}")