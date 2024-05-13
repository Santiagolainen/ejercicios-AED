__author__ = "Santiago"

import random

random.seed(49)

cont_mult_5 = 0
cont_mult_7 = 0
cont_mult_9 = 0
num_max_5_9 = 0
cont_num_pares = 0

for i in range(20000):
    n = random.randint(1, 45000)
    if n % 5 == 0:
        cont_mult_5 += 1
    if n % 7 == 0:
        cont_mult_7 += 1
    if n % 9 == 0:
        cont_mult_9 += 1

    ultimo_digito = n % 10
    if n > num_max_5_9 and 8 >= ultimo_digito >= 5:
        num_max_5_9 = n

    if n % 2 == 0 and n < 15000:
        cont_num_pares += 1

print(f"La cantidad de números múltiplos de 5 son: {cont_mult_5}")
print(f"La cantidad de números múltiplos de 7 son: {cont_mult_7}")
print(f"La cantidad de números múltiplos de 9 son: {cont_mult_9}")
print(f"El mayor número cuyo último dígito es mayor o igual a 5 pero menor a 8 es: {num_max_5_9}")
print(f"La cantidad de números pares menores a 15000 son: {cont_num_pares}")
print(f"Eso representa un total de {int((cont_num_pares*100)/20000)}%")
