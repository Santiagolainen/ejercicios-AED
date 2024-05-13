__author__ = "Santiago"

import random

n = int(input("Ingrese la cantidad de números aleatorios que desea calcular: "))

while n <= 0:
    print("Ingrese una cantidad mayor a 0")
    n = int(input("Ingrese la cantidad de números aleatorios que desea calcular: "))

cont_num_5 = 0
cont_num_pares = 0
min_num_mult_3 = None
primer_num = None
cont_primer_num = 0

for i in range(n):
    num = random.randint(1, 100)

    if num % 3 == 0 and min_num_mult_3 is None:
        min_num_mult_3 = num

    if i == 0:
        primer_num = num

    if num % 10 == 5:
        cont_num_5 += 1

    if num % 2 == 0:
        cont_num_pares += 1

    if num % 3 == 0 and num < min_num_mult_3:
        min_num_mult_3 = num

    if num == primer_num:
        cont_primer_num += 1

print(f"La cantidad de números que terminan en 5 son {cont_num_5}")
print(f"El porcentaje de números pares en la secuencia es de un {round((cont_num_pares*100)/n,2)}%")
print(f"El menor número múltiplo de 3 de la secuencia es: {min_num_mult_3}")
print(f"La cantidad de veces que apareció el primer número en la secuencia fue de {cont_primer_num} de veces")

