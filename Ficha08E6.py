__author__ = "Santiago"

import random

print("Menú de opciones y validación")
print("="*130)
print("1 - Ingresar números y calcular su promedio\t\t\t\t\t\t\t\t 2 - Generar n valores aleatorios entre -100 y 100")
print("3 - Cargar la nota de un alumno e informar si está aprobado o no\t\t 4 - Salir")
op = int(input())

while op != 4:
    if op == 1:
        cont_num = 0
        nums = 0
        promedio = 0
        n = int(input("Ingrese un número (con -1 finaliza la operación): "))
        while n != -1:
            cont_num += 1
            nums += n
            n = int(input("Ingrese un número (con -1 finaliza la operación): "))

        if cont_num != 0:
            promedio = nums/cont_num
        print(f"El promedio de todos los números es: {promedio}")
    elif op == 2:
        cont_num_negativos = 0
        cont_num_positivos = 0
        n = int(input("Ingrese la cantidad de números aleatorios que desea: "))
        for i in range(n):
            num = random.randint(-100, 100)
            if num > 0:
                cont_num_positivos += 1
            else:
                cont_num_negativos += 1
        print(f"La cantidad de valores positivos fue de {cont_num_positivos} números, y la cantidad de números negativos"
              f"fue de {cont_num_negativos}")
    elif op == 3:
        nota = float(input("Ingrese la nota del alumno: "))
        if nota > 10 or nota < 0:
            print("Nota no válida")
        else:
            if nota >= 4:
                print("El alumno está aprobado")
            else:
                print("El alumno está desaprobado")
    else:
        print("Opción no válida")
    print("\nMenú de opciones y validación")
    print("=" * 130)
    print(
        "1 - Ingresar números y calcular su promedio\t\t\t\t\t\t\t\t 2 - Generar n valores aleatorios entre -100 y 100")
    print("3 - Cargar la nota de un alumno e informar si está aprobado o no\t\t 4 - Salir")
    op = int(input())

print("Programa finalizado")