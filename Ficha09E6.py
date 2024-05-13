__author__ = "Santiago"

import random

random.seed(20220512)
cont_mult_3 = 0
cont_mult_5 = 0
cont_otro = 0
max_num_1 = 0
cont_num_11 = 0
num11 = 0


for i in range(25000):
    n = random.randint(1, 45000)

    if n % 3 == 0:
        cont_mult_3 += 1
    elif n % 5 == 0:
        cont_mult_5 += 1
    else:
        cont_otro += 1

    longitud = len(str(n)) - 1
    primer_digito = n//10**longitud
    if primer_digito == 1 and n > max_num_1:
        max_num_1 = n

    if n % 2 == 0 and n % 11 == 0:
        cont_num_11 += n
        num11 += 1

if num11 != 0:
    promedio = cont_num_11//num11
else:
    promedio = 0

print(f"La cantidad de números múltiplos de 3 son: {cont_mult_3}")
print(f"La cantidad de números múltiplos de 5 pero no de 3 son: {cont_mult_5}")
print(f"La cantidad de números que no cumplen con ninguna de las condiciones anteriores son: {cont_otro}")
print(f"El mayor entre todos los números que comienzan con el dígito 1 es: {max_num_1}")
print(f"El promedio de los números que son pares y múltiplos de 11 es: {promedio}")
print(f"El porcentaje que representa cada contador del punto 1 es: ")
print(f"Múltiplos de 3: {int((cont_mult_3*100)/25000)}%")
print(f"Múltiplos de 5: {int((cont_mult_5*100)/25000)}%")
print(f"Múltiplos de otros números: {int((cont_otro*100)/25000)}%")