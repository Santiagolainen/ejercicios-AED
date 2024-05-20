__author__ = "Santiago"

def numeros():

    nums = []
    num = int(input("Ingrese un número, si ingresa 0 se cancela el programa: "))

    while num != 0:
        nums.append(num)
        num = int(input("Ingrese un número, si ingresa 0 se cancela el programa: "))
    
    return nums

def num_div_4(nums):
    cont_nums_div_4 = 0
    for i in range(len(nums)):
        if nums[i] % 4 == 0:
            cont_nums_div_4 += 1
    return cont_nums_div_4

def may_num_impar(nums):
    may_num = 0
    for i in range(len(nums)):
        if nums[i] % 2 != 0 and nums[i] > may_num:
            may_num = nums[i]
    return may_num

def primer_num(nums):
    cont_primer_num = 0
    if len(nums) != 0:
        prim_num = nums[0]
        for i in range(len(nums)):
            if nums[i] == prim_num:
                cont_primer_num += 1
    return cont_primer_num

def sucesion_123(nums):
    cont_suc_123 = 0
    for i in range(len(nums) - 2):
        num_posterior = nums[i + 1]
        num_posterior2 = nums[i + 2]
        if nums[i] == 1 and num_posterior == 2 and num_posterior2 == 3:
            cont_suc_123 += 1
    
    return cont_suc_123


nums = numeros()
print(f"La cantidad de números que eran divisibles por 4 fueron: {num_div_4(nums)}")
print(f"El mayor de los números impares fue {may_num_impar(nums)}")
print(f"El primer número se ingresó {primer_num(nums)} de veces")
print(f"La cantidad de veces que se ingresó la sucesión 123 fue de {sucesion_123(nums)} veces")
