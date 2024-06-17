def suma_nums_par_recursiva(n):
    if n % 2 != 0:
        n = n - 1
    if n == 0:
        return 0
    return n + suma_nums_par_recursiva(n - 2)

def main():
    n = int(input('Ingrese el número entero que desea sumar: '))

    print(suma_nums_par_recursiva(n))


if __name__ == '__main__':
    main()