__author__ = "Santiago"

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

print("Orden ascendente")
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        print(i)

print("\nOrden descendente")
for i in range(n2 + 1, n1, -1):
    if i % 2 == 0:
        print(i)
