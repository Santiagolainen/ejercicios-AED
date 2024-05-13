__author__ = "Santiago"

import random

print("Secuencias, Menu y Texto\n")
print("="*80)
print("")
print("Ingrese por teclado lo que desea hacer\n")
print("1 - Ingresar una secuencia de números\t\t 2 - Ingresar un texto")
print("3 - Ingresar nombre y notas finales\t\t\t 4 - Salir")
op = int(input())

while op != 4:
    if op == 1:
        cont_mult_3_5 = 0
        n = int(input("Ingrese la cantidad de números: "))
        while n <= 0:
            print("Ingrese un valor mayor a 0")
            n = int(input("Ingrese la cantidad de números: "))

        for i in range(n):
            num = random.randint(1, 100)
            if num % 3 == 0 and num % 5 == 0:
                cont_mult_3_5 += 1

        print(f"La cantidad de números que son múltiplos de 3 y 5 son {cont_mult_3_5} números, eso "
              f"representa un {round((cont_mult_3_5*100)/n,2)}%")
    elif op == 2:
        cont_pal_4 = 0
        texto = input("Ingrese el texto que termine con un punto: ")
        while "." not in texto or texto == "":
            print("Texto no válido")
            texto = input("Ingrese el texto que termine con un punto: ")

        textoR = ""

        i = 0

        while texto[i] != ".":
            textoR += texto[i]
            i += 1

        textoL = textoR.split()

        for palabra in textoL:
            if len(palabra) > 4:
                cont_pal_4 += 1

        print(f"La cantidad de palabras con más de 4 letras son {cont_pal_4}")

    elif op == 3:
        nombre1 = input("Ingrese el nombre del primer alumno: ")
        nota1 = float(input("Ingrese la nota del alumno: "))
        nombre2 = input("Ingrese el nombre del segundo alumno: ")
        nota2 = float(input("Ingrese la nota del alumno: "))
        nombre3 = input("Ingrese el nombre del tercer alumno: ")
        nota3 = float(input("Ingrese la nota del alumno: "))

        alumnos = [(nombre1, nota1),
                   (nombre2, nota2),
                   (nombre3, nota3)]

        for i in range(len(alumnos)):
            for j in range(len(alumnos) - i - 1):
                if alumnos[j][1] < alumnos[j+1][1]:
                    alumnos[j + 1], alumnos[j] = alumnos[j], alumnos[j + 1]
        print(f"El alumno con la peor nota fue {alumnos[-1]}")


    else:
        print("Opción no válida")

    print("\nSecuencias, Menu y Texto\n")
    print("=" * 80)
    print("")
    print("Ingrese por teclado lo que desea hacer\n")
    print("1 - Ingresar una secuencia de números\t\t 2 - Ingresar un texto")
    print("3 - Ingresar nombre y notas finales\t\t\t 4 - Salir")
    op = int(input())

print("Cancelación del programa")

