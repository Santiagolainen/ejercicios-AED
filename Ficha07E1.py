__author__ = "Santiago"

num_ciclistas = int(input("Ingrese la cantidad de ciclistas: "))
record = int(input("Ingrese el tiempo record previo: "))
ganador = "Nadie"
tiempo_ganador = 0
tiempo_total = 0
b = 0

for i in range(num_ciclistas):
    nombre = input("Ingrese el nombre del ciclista: ")
    tiempo = int(input("Ingrese el tiempo que logró ese competidor: "))

    if i == 0:
        tiempo_ganador = tiempo

    if tiempo < tiempo_ganador:
        ganador = nombre
        tiempo_ganador = tiempo
    if tiempo < record:
        b = 1
    tiempo_total += tiempo

print(f"El ganador de la carrera fué: {ganador}")
print(f"El promedio entre todos los ciclistas fue de: {tiempo_total/num_ciclistas}")

if b == 1:
    print("Se superó el record")
else:
    print("No se superó el record")
