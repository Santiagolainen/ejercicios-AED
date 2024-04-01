__author__ = "Santiago"

c1 = float(input("Ingrese el cateto 1: "))
c2 = float(input("Ingrese el cateto 2: "))

print("La hipotenusa es:", round(pow(c1**2 + c2**2, 1/2), 3))
print("El lado mayor es:", max(c1, c2))
print("El lado menor es:", min(c1, c2))