__author__ = "Santiago"

minutos = 1
segundos = 52 + 2 + 59 + 48
centesimas = 15 + 75 + 80 + 15

minutos += segundos // 60
segundos = (segundos % 60) + (centesimas // 100)
centesimas = centesimas % 100

print(f"El tiempo total fue de {minutos} minutos, {segundos} segundos y {centesimas} centesimas")
