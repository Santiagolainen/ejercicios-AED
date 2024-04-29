__author__ = "Santiago"

n = int(input("Ingrese la cantidad de números: "))
nums_positivos = 0
num_negativo_max = None
num_menor = None
segundo_num_menor = None

for i in range(n):
    num = int(input("Ingrese un número: "))
    
    if num_menor == None or num_menor > num:
        num_menor = num
    
    if segundo_num_menor == None or num_menor < num < segundo_num_menor:
        segundo_num_menor = num

    if num > 0:
        nums_positivos += num

    if num < 0:
        if num_negativo_max == None or num > num_negativo_max:
            num_negativo_max = num

print(f"El segundo número menor es {segundo_num_menor}")
print(f"El promedio de los números positivos es de {nums_positivos/n}")
print(f"El mayor de los números negativos es {num_negativo_max}")