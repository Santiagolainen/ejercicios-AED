__author__ = "Santiago"

#Usando diccionario

hospital = {'Urgencias': 0.37, 'Pediatría': 0.42, 'Traumatología': 0.21}

presupuesto = int(input("Cargar el presupuesto del hospital: "))

for area, porcentaje in hospital.items():
    montoTotal = presupuesto * porcentaje
    print(f"El monto asignado para el area de {area} es de {montoTotal}")

#Usando tuples
print("")
hospitalT = (("Urgencias", 0.37), ("Pediatría", 0.42), ("Traumatología", 0.21))

for areaT, porcentajeT in hospitalT:
    montoTotalT = porcentajeT*presupuesto
    print(f"El monto asignado a {areaT} es de {montoTotalT}")