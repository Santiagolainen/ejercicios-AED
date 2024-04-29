__author__ = "Santiago"

import random

n = int(input("Ingrese la cantidad de números: "))

for i in range(n):
    num = random.randint(5000, 450000)
    hexadecimal = hex(num)
    print(f"El número {num} en hexadecimal es {hexadecimal[2:]}")