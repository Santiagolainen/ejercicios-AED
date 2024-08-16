import random

def prom_a_b(nums, a, b):
    sum = cont = 0
    while a <= b:
        sum += nums[a-1]
        a += 1
        cont += 1
    
    if cont != 0:
        return sum//cont
    return 0


def min_num_impar(nums):
    n = len(nums)
    men = None

    for i in range(n):
        if (men is None or men > nums[i]) and nums[i] % 2 != 0:
            men = nums[i]
    
    return men


def mostrar_num_mult(x, nums):
    n = len(nums)

    for i in range(n):
        if nums[i] % x == 0:
            print(f'{nums[i]}, ', end="")
    


def main():
    
    op = 0
    nums = []

    while op != 5:
        print('')
        print('==='*16 + ' MENU DE OPCIONES ' + '==='*16)
        print('1 - Carga de datos\t\t\t2 - Mostrar promedio de números comprendido entre 2 valores ingresados')
        print('3 - Mostrar menor número impar \t\t4 - Mostrar todos los número múltiplos de un número ingresado')
        print('5 - Salir')
        op = int(input())

        if op == 1:
            n = int(input('Ingrese cuántos numeros desea cargar: '))
            
            for i in range(n):
                nums.append(random.randint(1, 300))
            print(nums)
        elif op == 2:
            print('Ingrese un rango de a-b para calcular el promedio entre esos números')
            a = int(input('a: '))
            b = int(input('b: '))
            while a > b or b > len(nums) + 1:
                print('Rango no válido')
                a = int(input('a: '))
                b = int(input('b: '))
            promedio = prom_a_b(nums, a, b)
            print(f'El promedio entre los valores desde {a} hasta {b} es: {promedio}')
        elif op == 3:
            men = min_num_impar(nums)
            print(f'El menor número impar es {men}')
        elif op == 4:
            x = int(input('Ingrese el número que desea buscar los múltiplos: '))
            mostrar_num_mult(x, nums)
        elif op > 5:
            print('Número no válido')

    print('Programa finalizado...')


if __name__ == '__main__':
    main()