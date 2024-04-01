__author__ = "Santiago"

anguloA = input("Ingrese el primer ángulo en ° ' '': ")
anguloB = input("Ingrese el segundo ángulo en ° ' '': ")

horaA = ""
horaB = ""
minutosA = ""
minutosB = ""
segundosA = ""
segundosB = ""

iA = 0
iB = 0

while anguloA[iA] != "°":
    horaA += anguloA[iA]
    iA += 1

iA += 1

while anguloA[iA] != "'":
    minutosA += anguloA[iA]
    iA += 1

iA += 1

while iA < len(anguloA) - 2:
    segundosA += anguloA[iA]
    iA += 1

while anguloB[iB] != "°":
    horaB += anguloB[iB]
    iB += 1

iB += 1

while anguloB[iB] != "'":
    minutosB += anguloB[iB]
    iB += 1

iB += 1

while iB < len(anguloA) - 2:
    segundosB += anguloB[iB]
    iB += 1

segundosTotal = int(segundosA) + int(segundosB)
minutosTotal = int(minutosA) + int(minutosB)
horasTotal = int(horaA) + int(horaB)

if segundosTotal / 60 > 1:
    segundosTotal = segundosTotal % 60
    minutosTotal += 1

if minutosTotal / 60 > 1:
    minutosTotal = minutosTotal % 60
    horasTotal += 1

print(f"La suma de los ángulos A y B es: {horasTotal}° {minutosTotal}' {segundosTotal}''")
