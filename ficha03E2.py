__author__ = "Santiago"

fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
dia = ""
i = 0
while fecha[i] != "/":
    dia += fecha[i]
    i += 1
mes = ""
i += 1
while fecha[i] != "/":
    mes += fecha[i]
    i += 1
year = ""
i += 1
while i < len(fecha):
    year += fecha[i]
    i +=1
mesInt = int(mes)
if len(dia) > 2 or mesInt > 12:
    print("Formato invalido")
else:
    print("Día:", dia, "Mes:", mes, "Año:", year)


