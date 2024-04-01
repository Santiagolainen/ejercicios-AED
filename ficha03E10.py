__author__ = "Santiago"

natacion = input("Ingrese el tiempo logrado en natación en formato mm:ss minutos y segundos: ")
ciclismo = input("Ingrese el tiempo logrado en ciclismo en formato mm:ss minutos y segundos: ")
pedestre = input("Ingrese el tiempo logrado en pie en formato mm:ss minutos y segundos: ")

i = 0
j = 0
k = 0

natacionMinutos = ""
ciclismoMinutos = ""
pedestreMinutos = ""
natacionSegundos = ""
ciclismoSegundos = ""
pedestreSegundos = ""

while natacion[i] != ":":
    natacionMinutos += natacion[i]
    i += 1

i += 1

while i < len(natacion):
    natacionSegundos += natacion[i]
    i += 1

while ciclismo[j] != ":":
    ciclismoMinutos += ciclismo[j]
    j += 1

j += 1

while j < len(ciclismo):
    ciclismoSegundos += ciclismo[j]
    j += 1

while pedestre[k] != ":":
    pedestreMinutos += pedestre[k]
    k += 1

k += 1

while k < len(pedestre):
    pedestreSegundos += pedestre[k]
    k += 1

totalNatacion = (int(natacionMinutos) * 60) + int(natacionSegundos)
totalCiclismo = (int(ciclismoMinutos) * 60) + int(ciclismoSegundos)
totalPedestre = (int(pedestreMinutos) * 60) + int(pedestreSegundos)

totalPrueba = totalNatacion + totalCiclismo + totalPedestre
horas = totalPrueba // 3600
minutos = (totalPrueba % 3600) // 60
segundos = (totalPrueba % 3600) % 60

print(f"Tiempo total de la prueba: {horas}:{minutos}:{segundos}")
print(f"Tiempo máximo: {max(totalNatacion, totalCiclismo, totalPedestre)} segundos\nTiempo mínimo: {min(totalNatacion, totalCiclismo, totalPedestre)} segundos")
print(f"Tiempo promedio de la prueba: {round(totalPrueba/3,2)} segundos")
