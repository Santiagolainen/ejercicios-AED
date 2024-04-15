__author__ = "Santiago"

# Ingreso de valores por teclado
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese un número: "))

# Chequeo de mayor número
if n1 > n2 and n1 > n3:
    may = n1
elif n2 > n3:
    may = n2
else:
    may = n3

print("El mayor número es:", may)