def menu():
    print('Seleccione si quiere hacer la sucesion de fibonacci de forma recursiva o iterativa:')
    print('1 - Recursiva')
    print('2 - Iterativa')
    op = int(input())
    while op != 1 and op != 2:
        print('Eliga una opción válida')
        op = int(input())
    
    return op 

def factorial_recursiva(n):
    if n == 0:
        return 1
    return factorial_recursiva(n-1)*n

def factorial_iterativa(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f 

def fibonacci_recursiva(n):
    if n <= 1:
        return 1
    return fibonacci_recursiva(n - 1) + fibonacci_recursiva(n - 2)

def fibonacci_iterativa(n):
    ant1 = ant2 = 1
    for i in range(2, n):
        resultado = ant1 + ant2
        ant2 = ant1
        ant1 = resultado
        
    return ant1 

def mostrar_nums_recursiva(n):
    if n > 0:
        mostrar_nums_recursiva(n-1)
        print('Numero:',n)

def mostrar_nums_iterativa(n):
    for i in range(n, 0, -1):
        print('Numero:', i)
        
        

def main():
    op = menu()
    n = int(input('Ingrese el número que desea calcular: '))

    if op == 1:
        num_fibonacci = fibonacci_recursiva(n)
        num_factorial = factorial_recursiva(n)
        mostrar_nums_recursiva(n)
    elif op == 2:
        num_fibonacci = fibonacci_iterativa(n)
        num_factorial = factorial_iterativa(n)
        mostrar_nums_iterativa(n)
        
    print(num_fibonacci)
    print(num_factorial)


if __name__ == '__main__':
    main()