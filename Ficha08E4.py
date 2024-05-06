__author__ = "Santiago"

n = int(input("Ingrese un número (si ingresa 0 se corta el programa): "))
cont_num_6 = num_6 = num_div_exacto = cont_sec_num_asc = 0
nums = []

while n != 0:
    nums.append(n)
    n = int(input("Ingrese un número (si ingresa 0 se corta el programa): "))

for i in range(len(nums)):
    if nums[i] % 6 == 0:
        cont_num_6 += 1
        num_6 += nums[i]

    if i != 0 and nums[i] % nums[i - 1] == 0:
        num_div_exacto += 1

    if nums[i] % 2 != 0:
        if i > 3:
            if nums[i - 1] % 2 != 0 and nums[i - 2] % 2 != 0 and nums[i] > nums[i - 1] > nums[i - 2]:
                cont_sec_num_asc += 1

if cont_num_6 != 0:
    print(f"\nEl promedio de los números que son múltiplos de 6 es: {num_6/cont_num_6}")
else:
    print("No hay numeros múltiplos de 6")
print(f"\nLa cantidad de números que son divisores exactos del anterior son: {num_div_exacto}")
print(f"\nLa cantidad de veces que se generó una secuencia ascendente de 3 o más números impares fue de: {cont_sec_num_asc}")
