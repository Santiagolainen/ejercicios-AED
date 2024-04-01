__author__ = "Santiago"

distanciaFinalKm = 3641.3

x = float(input("Ingrese la cantidad de metros que realizó el viajero: "))

kmRecorridos = x/1000
porcentajeRecorrido = (x*100)/(distanciaFinalKm*1000)

print(f"Nuestro aventurero solo pudo hacer {kmRecorridos}km o {x} metros, eso representa un {porcentajeRecorrido}% del viaje")