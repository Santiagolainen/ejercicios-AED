def ingreso_nums():
    n = int(input('Ingrese los números (Si ingresa 0 se cancela el programa): '))
    nums = []
    while n != 0:
        nums.append(n)
        n = int(input())
    
    return nums

def por_nums_par(nums):
    cont_nums_par = 0
    porcentaje = 0
    for i in nums:
        if i % 2 == 0:
            cont_nums_par += 1
    if len(nums) != 0:
        porcentaje = (cont_nums_par*100)/len(nums)
    return porcentaje

def nums_ult_4_5(nums):
    cont_nums_4_5 = 0
    for i in nums:
        if i % 10 == 4 or i % 10 == 5:
            cont_nums_4_5 += 1
    
    return cont_nums_4_5

def men_num_div_3(nums):
    min_num_div_3 = None
    for i in nums:
        if min_num_div_3 == None and i % 3 == 0:
            min_num_div_3 = i
        if min_num_div_3 != None and i % 3 == 0 and i < min_num_div_3:
            min_num_div_3 = i
    
    return min_num_div_3

def sec_nums_7(nums):
    nums_7 = True
    for i in nums:
        if i > 7:
            nums_7 = False
    
    return nums_7

def main():
    nums = ingreso_nums()
    porcentaje = por_nums_par(nums)
    ult_dig_4_5 = nums_ult_4_5(nums)
    min_num_div_3 = men_num_div_3(nums)
    nums_7 = sec_nums_7(nums)
    print(f'El porcentaje de números pares es {porcentaje}%')
    print(f'La cantidad de números con úlimo dígito igual a 4 o a 5 son: {ult_dig_4_5}')
    print(f'El menor número divisible por 3 es: {min_num_div_3}')
    if nums_7 == True:
        print('La secuencia está compuesta unicamente por números menores o igual a 7')
    else:
        print('La secuencia tiene al menos un número mayor a 7')

main()