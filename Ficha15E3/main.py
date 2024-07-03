import arreglos
import funciones

def main():
    n = int(input('Ingrese la cantidad de números que desea procesar: '))
    nums = [0]*n
    nprimos = []
    total_nums = 0
    arreglos.array(nums)

    for num in nums:
        funciones.nums_prim(num, nprimos)
        total_nums += num
    
    promedio = funciones.prom(total_nums, len(nums))

    print(f'Los números primos son {nprimos}')
    print(f'El promedio de los números es de {promedio}')



if __name__ == '__main__':
    main()
