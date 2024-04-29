__author__ = "Santiago"

cuenta = input("Ingrese su email: ")
b = 0

if cuenta[0] == "@" or cuenta[-1] == "@" or cuenta[0] == "." or cuenta[-1] == "." or "@" not in cuenta or ".." in cuenta:
    b = 1

if b == 0:
    print("Cuenta válida")
else:
    print("Cuenta no válida")