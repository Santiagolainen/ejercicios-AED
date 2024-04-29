__author__ = "Santiago"

n = int(input("Ingrese la cantidad de barcos: "))
total_veleros = 0
total_lanchas = 0
monto_total = 0
max_mensual_velero = 0
nombre = ""

for i in range(n):
    nombre = input("Ingrese el nombre: ")
    tipo = int(input("Ingrese el tipo (1: velero, 2: lancha): "))
    monto_mensual = int(input("Ingrese el monto que paga por mes en guardería: "))
    monto_total += monto_mensual

    if tipo == 1:
        total_veleros += monto_mensual
        if max_mensual_velero < monto_mensual:
            max_mensual_velero, nombre_max_mensual_velero = monto_mensual, nombre
    elif tipo == 2:
        total_lanchas += monto_mensual

print(f"\nEl total anual aportado por los veleros es de: {total_veleros*12}")
print(f"\nEl total anual aportado por las lanchas es de: {total_lanchas*12}")
print(f"\nEl velero que mayor cuota paga es {nombre_max_mensual_velero} y su cuota es de {max_mensual_velero}")
print(f"\nEl promedio de cuota pagada por las embarcaciones es de: {round(monto_total/n,3)}")
print(f"\nEl porcentaje que representa el monto mensual recaudado por los veleros sobre el total mensual recaudado es de {round((total_veleros*100)/monto_total,2)}%")
print(f"\nEl porcentaje que representa el monto mensual recaudado por las lanchas sobre el total mensual recaudado es de {round((total_lanchas*100)/monto_total,2)}%")