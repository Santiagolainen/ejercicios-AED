__author__ = "Santiago"

nombres_meses = {1: "Enero",
                 2: "Febrero",
                 3: "Marzo",
                 4: "Abril",
                 5: "Mayo",
                 6: "Junio"}

sueldo_max = 0
sueldo_min = 0
mes_min = 0
sueldo_total = 0

for i in range(1,7):
    sueldo = int(input(f"Ingrese el sueldo para el mes de {nombres_meses[i]}: "))

    if sueldo > sueldo_max:
        sueldo_max = sueldo

    if sueldo < sueldo_min or i == 1:
        sueldo_min, mes_min = sueldo, nombres_meses[i]
    sueldo_total += sueldo

print(f"El aguinaldo es de {sueldo_max/2}")
print(f"El sueldo más bajo lo recibio en el mes de {mes_min}")
print(f"El sueldo promedio fue de: ${round(sueldo_total/6,2)}")
