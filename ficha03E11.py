__author__ = "Santiago"

palabra = input("Ingrese una palabra: ")

palabraEnmascarada = palabra[0]

i = 1

for i in range(len(palabra) - 2):
    palabraEnmascarada += "*"

palabraEnmascarada += palabra[-1]

print(palabraEnmascarada)