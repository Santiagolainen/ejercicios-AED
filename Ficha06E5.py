__author__ = "Santiago"

import random

i = 0
num_max = 0
num_positivos = 0

while i < 10000:
    num_random = random.randint(-100000, 100000)
    if num_random > num_max:
        num_max = num_random
    if num_random > 0:
        num_positivos += 1
    i += 1

por_num_positivos = (num_positivos * 100) / 10000

print(f"El número más grande fue: {num_max}")
print(f"El porcentaje de números positivos fue de: %{por_num_positivos}")
