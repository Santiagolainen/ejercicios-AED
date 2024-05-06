__author__ = "Santiago"

import random

random.seed(37)

cont_nums_rango20_5 = cont_nums_rango5_15 = cont_nums_rango15_9 = cont_nums_may_1000 = nums_may_1000 = may_impar = nums_div_7 = 0

for i in range(27000):
    num = random.randint(-20000, 30000)
    if -5000 > num >= -20000:
        cont_nums_rango20_5 += 1
    elif 15000 > num >= -5000:
        cont_nums_rango5_15 += 1
    elif num >= 15000 and num % 9 == 0:
        cont_nums_rango15_9 += 1

    if num >= 1000 and (num % 10 == 4 or num % 10 == 6):
        cont_nums_may_1000 += 1
        nums_may_1000 += num

    if num > 0 and num % 10 != 1 and num > may_impar and num % 2 != 0:
        may_impar = num

    if num % 7 == 0:
        nums_div_7 += 1

print(f"\nLa cantidad de números mayores o igales que -20000 pero menores que -5000 son {cont_nums_rango20_5}")
print(f"La cantidad de números mayores o iguales a -5000 pero menores que 15000 son {cont_nums_rango5_15}")
print(f"La cantidad de números mayores o iguales a -15000 y que además son divisibles por 9 son {cont_nums_rango15_9}")
print(f"\nEl promedio de los números generados mayor a 1000 pero que además tienen su último dígito igual a 4 o 6 es {int(nums_may_1000/cont_nums_may_1000)}")
print(f"\nEl mayor entre todos los números generados que sean positivos impares y que además tienen su último dígito diferente de 1 "
      f"es de {may_impar}")
print(f"\nEl porcentaje entero que la cantidad de números divisibles por 7 representa por sobre la cantidad total de números es de {int((nums_div_7*100)/27000)}%")