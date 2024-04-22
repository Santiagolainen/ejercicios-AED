__author__ = "Santiago"

ventas = int(input("Ingrese el total de ventas del vendedor: "))
categoria = int(input("Ingrese la categoría del vendedor (1-4) (si la categoría es 0 se cancela el programa): "))
ventas1 = 0
ventas2 = 0
ventas3 = 0
ventas4 = 0
ventasTotal = 0

while categoria != 0:
    if categoria > 4 or categoria < 0:
        print("Categoría no válida")
    else:
        if categoria == 1:
            ventasTotal += ventas
            ventas1 += (10*ventas)/100
        elif categoria == 2:
            ventasTotal += ventas
            ventas2 += (25 * ventas) / 100
        elif categoria == 3:
            ventasTotal += ventas
            ventas3 += (30 * ventas) / 100
        else:
            ventasTotal += ventas
            ventas4 += (40 * ventas) / 100

    ventas = int(input("Ingrese el total de ventas del vendedor: "))
    categoria = int(input("Ingrese la categoría del vendedor (1-4) (si la categoría es 0 se cancela el programa): "))


print(f"La cantidad total de ventas fue de {ventasTotal} ventas")
print(f"A la categoría uno se le debe pagar {ventas1} - A la categoría dos se le debe pagar {ventas2} - A la "
      f"categoría tres se le debe pagar {ventas3} - A la categoría cuatro se le debe pagar {ventas4}")
