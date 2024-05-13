__author__ = "Santiago"

import random

random.seed(11)
cont_num_div_4 = 0
cont_num_div_8_4 = 0
cont_num_2000 = 0
num_2000 = 0
promedio = 0
primer_num = None
cont_num_menos_primero = 0
b_valores_extremos = False

for i in range(1000):
    n = random.randint(1, 2500)

    if i == 0:
        primer_num = n

    if n % 4 == 0 and n % 8 != 0:
        cont_num_div_4 += 1

    if n % 8 == 0 and n % 4 == 0:
        cont_num_div_8_4 += 1

    if n > 2000:
        num_2000 += n
        cont_num_2000 += 1

    if i != 0 and n < primer_num:
        cont_num_menos_primero += 1

    if n == 1 or n == 2500:
        b_valores_extremos = True

if cont_num_2000 != 0:
    promedio = num_2000/cont_num_2000

print(f"Los números divisibles por 4 pero no por 8 son: {cont_num_div_4}")
print(f"Los números divisibles por 4 y 8 son: {cont_num_div_8_4}")
print(f"El promedio de los valores mayores a 2000 es: {int(promedio)}")
print(f"La cantidad de números menores al primer valor son: {cont_num_menos_primero}, eso representa "
      f"un {int((cont_num_menos_primero*100)/1000)}%")
if b_valores_extremos:
    print("Aparecieron los valores extremos del intervalo")
else:
    print("No aparecieron los valores extremos del intervalo")