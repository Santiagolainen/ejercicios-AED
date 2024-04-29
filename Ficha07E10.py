__author__ = "Santiago"

patente = input("Ingrese la patente: ")
b = 0
letras = 0
tipo_patente = 0

if " " in patente:
    b = 1

if len(patente) == 6:
    for i in range(0,3):
        if patente[i].isdigit():
            b = 1
    for i in range(3, 6):
        if not patente[i].isdigit():
            b = 1
    tipo_patente = "antigua"
elif len(patente) == 7:
    for i in range(0,2):
        if patente[i].isdigit():
            b = 1
    for i in range(2, 5):
        if not patente[i].isdigit():
            b = 1
    for i in range(5, 7):
        if patente[i].isdigit():
            b = 1
    tipo_patente = "nueva"
else:
    b = 1
    
if b == 1:
    print("Patente no válida")
else:
    print(f"Patente válida. Es una patente {tipo_patente}")
