__author__ = "Santiago"

def numeros():

    nums = []
    num = int(input("Ingrese un número, si ingresa 0 se cancela el programa: "))

    while num != 0:
        nums.append(num)
        num = int(input("Ingrese un número, si ingresa 0 se cancela el programa: "))
    
    return nums

def may_n1(nums, n1):
    cont_n1 = 0
    for i in range(len(nums)):
        if nums[i] > n1:
            cont_n1 += 1
    return cont_n1

def men_n2(nums, n2):
    cont_n2 = 0
    for i in range(len(nums)):
        if nums[i] < n2:
            cont_n2 += 1
    return cont_n2

def impar_par(nums):
    b_impar_par = False
    if len(nums) > 1:
        for i in range(len(nums) - 1):
            num_posterior = nums[i + 1]
            if nums[i] % 2 != 0 and num_posterior % 2 == 0:
                b_impar_par = True
    
    return b_impar_par

def dos_5(nums):
    cont_5 = 0
    if len(nums) > 1:
        for i in range(len(nums) - 1):
            num_posterior = nums[i + 1]
            if nums[i] == 5 and num_posterior == 5:
                cont_5 += 1

    return cont_5

nums = numeros()
n1 = int(input("Ingrese n1: "))
n2 = int(input("Ingrese n2: "))
nums_may_n1 = may_n1(nums, n1)
porcentaje_n1 = (nums_may_n1*100)/len(nums)
nums_men_n2 = men_n2(nums, n2)
porcentaje_n2 = (nums_men_n2*100)/len(nums)
print(f"La cantidad de números mayores que n1 fueron {nums_may_n1}, eso representa un {porcentaje_n1}% sobre el total de números")
print(f"La cantidad de números menores a n2 fueron {nums_men_n2}, eso representa un {porcentaje_n2}% sobre el total de números")
if impar_par(nums) == True:
    print("Se ingreso un impar seguido de un par")
else:
    print("No se ingresó un impar seguido de un par")
print(f"La cantidad de veces que se ingresó un 5 seguido de otro fueron {dos_5(nums)} veces")
