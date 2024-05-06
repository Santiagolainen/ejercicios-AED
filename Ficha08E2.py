__author__ = "Santiago"

nums = int(input("Ingrese un número (si ingresa 0 se corta el programa): "))
nums_div_3 = 0
nums_cuadrado = 0
may = 0
mayP = 0
total = 0
num_anterior = 0
while nums != 0:
    if nums % 3 == 0:
        nums_div_3 += 1
    if total != 0 and pow(num_anterior,2) == nums:
        nums_cuadrado += 1
    if total == 0 or may < nums and nums % 2 != 0:
        may = nums
        mayP = total
    total += 1
    num_anterior = nums
    nums = int(input("Ingrese un número (si ingresa 0 se corta el programa): "))

print(f"El porcentaje que representan los números divisibles por 3 sobre el total de numeros ingresados es "
      f"del {round((nums_div_3*100)/total,2)}%")
print(f"La cantidad de números que son el cuadrado del anterior son: {nums_cuadrado}")
print(f"El mayor elemento impar es {may} y se encuentra en la posición {mayP + 1}")

