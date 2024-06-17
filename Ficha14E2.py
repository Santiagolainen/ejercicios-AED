def suma_nums_recursiva(n):
    if n == 0:
        return 0
    return n + suma_nums_recursiva(n-1)

def main():
    n = int(input('Ingrese el número entero que desea sumar: '))

    print(suma_nums_recursiva(n))


if __name__ == '__main__':
    main()