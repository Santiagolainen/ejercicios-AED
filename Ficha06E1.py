__author__ = "Santiago"

espectadores = int(input("Ingrese la cantidad de expectadores (si son 0 se termina el programa): "))
cont = 0
funciones = 0
total_dinero = 0

while espectadores != 0:
    descuento = input('Ingrese "S" si hay descuento, si no lo hay ingrese "N": ')
    if descuento == "S" or descuento == "s":
        total_dinero = espectadores * 50
        cont += 1
    elif descuento == "N" or descuento == "n":
        total_dinero = espectadores * 75
    funciones += 1
    espectadores = int(input("Ingrese la cantidad de expectadores (si son 0 se termina el programa): "))

por_funciones_descuento = 0

if funciones != 0:
    por_funciones_descuento = (cont * 100)/funciones

print(f"El total recaudado fue de: {total_dinero}$")
print(f"Se efectuaron {cont} funciones con descuento, eso representa el %{por_funciones_descuento} total de funciones")

