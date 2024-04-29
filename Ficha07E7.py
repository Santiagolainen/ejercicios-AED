__author__ = "Santiago"

import random

even_max = 0
odd_min = 0

for i in range(0,8):
    num = random.randint(1,100)

    print(num)

    if num % 2 == 0:
        if num > even_max:
            even_max = num
    else:
        if num < odd_min or odd_min == 0:
            odd_min = num

print(f"El mayor número par fue {even_max}")
print(f"El menor número impar fue {odd_min}")