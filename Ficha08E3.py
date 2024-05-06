__author__ = "Santiago"

n = int(input("Ingrese un número (si ingresa 0 se cancela el programa): "))
i = 0
num_anterior = nums5 = primer_num = nums_mayor = cont_primer_num = 0
primer_num = n

if n != 0:
    i = 1

while n != 0:
    if n % 10 == 5:
        nums5 += 1
    if n == primer_num:
        cont_primer_num += 1
    if n > num_anterior:
        nums_mayor += 1
    num_anterior = n
    n = int(input("Ingrese un número (si ingresa 0 se cancela el programa): "))
if n != 0:
    cont_primer_num = cont_primer_num - 1
    nums_mayor = nums_mayor - 1

print(f"\nLa cantidad de números que terminan en 5 son {nums5}\n")
print(f"La cantidad de veces que aparece el primer número son {cont_primer_num}\n")
print(f"La cantidad de números que son mayores a su antecesor son {nums_mayor}")