__author__ = "Santiago"

print("Programa para saber discriminante b²-4ac")
print("Si desea finalizar el programa presione cualquier tecla no numérica")

continuar = "S"
cont_2_raices = 0
cont_1_raiz = 0
cont_num_im = 0
total_raices = 0

while continuar == "S" or continuar == "s":

    a = float(input("Ingrese el valor a: "))
    b = float(input("Ingrese el valor b: "))
    c = float(input("Ingrese el valor c: "))

    formula = b**2 - 4*a*c
    print(f"La discriminante es igual a: {formula}")

    if formula != 0:
        cont_2_raices += 1
    else:
        cont_1_raiz += 1

    if formula < 0:
        cont_num_im += 1

    total_raices += 1
    continuar = input("Si desea continuar presione 'S' sino presione otra tecla: ")

print(f"La cantidad de discriminantes que darán 2 raices son: {cont_2_raices}")
print(f"La cantidad de discriminantes que darán 1 raíz son: {cont_1_raiz}")
print(f"La cantidad de discriminantes que darán raíces en el campo de los números imaginarios es: {cont_num_im}, eso "
      f"representa un %{(cont_num_im * 100)/total_raices}")