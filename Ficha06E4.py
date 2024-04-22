__author__ = "Santiago"

import random

i = 0
suma_num = 0

while i < 100000:
    num_random = random.randint(0, 100000)
    suma_num += num_random
    i += 1

print(f"El promedio de la suma de 100000 número al azar es: {suma_num/100000}")