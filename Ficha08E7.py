__author__ = "Santiago"

import random

random.seed(76)
nums_par_mult_6 = 0
primer_num = None
nums_mayores_primer = 0
cont_nums_segundo_millar = 0

for i in range(5000):
    n = random.randint(1, 65000)

    if primer_num is None:
        primer_num = n

    if n % 2 == 0 and n % 6 == 0:
        nums_par_mult_6 += 1

    if i != 0 and n > primer_num:
        nums_mayores_primer += 1

    if 2000> n > 1000:
        cont_nums_segundo_millar += 1

print(f"La cantidad de números pares que son múltiplos de 6 son {nums_par_mult_6} números")
print(f"La cantidad de números mayores al primer número de la serie son {nums_mayores_primer} números")
print(f"La cantidad de números que pertenecen al segundo millar de números son {cont_nums_segundo_millar} números")
print(f"El porcentaje de de números mayores al primer número de la serie es de un {round((nums_mayores_primer*100)/5000,2)}")