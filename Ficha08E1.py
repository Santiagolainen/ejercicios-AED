__author__ = "Santiago"

op = int(input("                                 Menu de Opciones\n"
               "==================================================================================\n"
               "1 - Mostrar suma de cuadrados de números\n2 - Determinar cantidad de palabras que "
               "finalizan con vocales\n3 - Determinar si hay mayor cantidad de valores pares o impares\n4 - Salir\n"))
while op != 4:
    if op == 1:
        print("Suma de cuadrados de números ingresados por teclado")
        n = int(input("Ingrese la cantidad de números naturales que desea sumar su cuadrado (debe ser mayor a 0): "))
        i = 0
        suma = 0
        while i < n:
            num = int(input("Ingrese un número: "))
            if num > 0:
                suma += pow(num, 2)
                i += 1
            else:
                print("Ingrese un valor mayor a 0")
        print(f"La suma de los cuadrados de todos los números es de {suma}")
    elif op == 2:
        print("Cantidad de palabras que finalizan con una vocal")
        texto = input("Ingrese el texto con un punto al final: ")
        textoM = texto.lower()
        palabras = 0
        vocales = ("a", "e", "i", "o", "u")
        i = 1
        if len(textoM) == 0:
            print("Texto no válido")
        else:
            if "." not in textoM:
                print("La oración no tiene un punto al final")
            else:
                while textoM[i] != ".":
                    if textoM[i] == " " and textoM[i - 1] in vocales:
                        palabras += 1
                        i += 1
                    else:
                        i += 1
                if textoM[i - 1] in vocales:
                    palabras += 1
                print(f"La cantidad de palabras que finalizan con una vocal son {palabras}")
    elif op == 3:
        num = int(input("Ingrese un número (La carga finaliza si se ingresa 0): "))
        par = 0
        impar = 0
        while num != 0:
            if num % 2 == 0:
                par += 1
            else:
                impar += 1
            num = int(input("Ingrese un número (La carga finaliza is se ingresa 0): "))
        if par > impar:
            print("Hay mayor cantidad de números pares que impares")
        else:
            print("Hay mayor cantidad de número impares que pares")
    else:
        print("Operación desconocida")
    op = int(input("\n                                 Menu de Opciones\n"
                   "==================================================================================\n"
                   "1 - Mostrar suma de cuadrados de números\n2 - Determinar cantidad de palabras que "
                   "finalizan con vocales\n3 - Determinar si hay mayor cantidad de valores pares o impares\n4 - Salir\n"))
print("Cancelación del programa")
