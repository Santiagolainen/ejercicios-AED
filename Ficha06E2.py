__author__ = "Santiago"

cont = 0
total_ventas = 0
ventas_100_300 = 0
ventas_400_600 = 0
ventas_50 = 0

ventas = int(input("Ingrese la cantidad de ventas que hubo (si es un número negativo se cancela el programa): "))

while ventas > 0:
    cont += 1
    total_ventas += ventas
    if 300 > ventas > 100:
        ventas_100_300 += 1
    elif 600 > ventas > 400:
        ventas_400_600 += 1
    elif ventas < 50:
        ventas_50 = 1

    ventas = int(input("Ingrese la cantidad de ventas que hubo (si es un número negativo se cancela el programa): "))

print(f"La cantidad de ventas fue: {cont}")
print(f"El total de ventas fue: {total_ventas}")
print(f"Las ventas cuyos valores fueron de entre 100 y 300 fue: {ventas_100_300}")
print(f"Las ventas con 400,500 y 600 unidades fueron: {ventas_400_600}")

if ventas_50 == 1:
    print("Hubieron ventas menores a 50 unidades")
