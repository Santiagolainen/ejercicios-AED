__author__ = "Santiago"

partida = input("Ingrese el horario de partida del vuelo en formato 00:00 y 24hs: ")
llegada = input("Ingrese el horario de llegada del vuelo en formato 00:00 y 24hs: ")

horaPartida = ""
minutosPartida = ""

i = 0
while partida[i] != ":":
    horaPartida += partida[i]
    i += 1

i += 1
while i < len(partida):
    minutosPartida += partida[i]
    i += 1

horaLlegada = ""
minutosLlegada = ""
j = 0
while llegada[j] != ":":
    horaLlegada += llegada[j]
    j += 1

j += 1
while j < len(llegada):
    minutosLlegada += llegada[j]
    j += 1

horaPartidaint = int(horaPartida)
horaLlegadaint = int(horaLlegada)
minutosPartidaInt = int(minutosPartida)
minutosLlegadaInt = int(minutosLlegada)

horasTotal = horaLlegadaint - horaPartidaint
minutosTotal = minutosLlegadaInt - minutosPartidaInt

if horaPartidaint >= horaLlegadaint:
    horaLlegadaint += 24
    horasTotal = horaLlegadaint - horaPartidaint

horasAMinutos = horasTotal * 60
minutosVuelos = horasAMinutos + minutosTotal

calcLlegadaHotel = minutosLlegadaInt + 45
llegadaHotelMinutosint = 0
if calcLlegadaHotel < 60:
    llegadaHotelMinutosint = calcLlegadaHotel
else:
    moduloLlegada = calcLlegadaHotel % 60
    horaLlegadaint += 1
    llegadaHotelMinutosint = moduloLlegada

if horaPartidaint >= 24 or minutosPartidaInt >= 60 or horaLlegadaint >= 24 or minutosLlegadaInt >= 60:
    print("Formato de hora invalido")
else:
    print("El vuelo duró:", minutosVuelos, "minutos")
    print(f"El viajero llego al hotel a las: {horaLlegadaint}:{llegadaHotelMinutosint}")
