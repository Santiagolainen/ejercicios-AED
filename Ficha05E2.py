__author__ = "Santiago"

# Ingreso de datos por teclado
b = 0

form1 = input("Ingrese la primera fórmula: ")
vot1 = int(input("Ingrese la cantidad de votos de la primera fórmula: "))

form2 = input("Ingrese la segunda fórmula: ")
vot2 = int(input("Ingrese la cantidad de votos de la segunda fórmula: "))

form3 = input("Ingrese la tercera fórmula: ")
vot3 = int(input("Ingrese la cantidad de votos de la tercera fórmula: "))

votos_total = vot1 + vot2 + vot3

por_v1 = round((vot1 * 100) / votos_total, 2)
por_v2 = round((vot2 * 100) / votos_total, 2)
por_v3 = round((vot3 * 100) / votos_total, 2)

votPartidos = [[form1, vot1, por_v1], [form2, vot2, por_v2], [form3, vot3, por_v3]]
votPartidos.sort(key=lambda x: x[1], reverse=True)

segundoPartido = votPartidos[1]

partidoMax = max(votPartidos, key=lambda x: x[1])

if partidoMax[2] > 45:
    b = 1
    partidoGanador = partidoMax[0]
    votosGanador = partidoMax[1]
    porcentajeGanador = partidoMax[2]
else:
    partido1 = partidoMax[0]
    votosPartido1 = partidoMax[1]
    porcentajePartido1 = partidoMax[2]
    partido2 = segundoPartido[0]
    votosPartido2 = segundoPartido[1]
    porcentajePartido2 = segundoPartido[2]

if b == 1:
    print(f"El partido {partidoGanador} ganó en primera vuelta con un {porcentajeGanador}% de votos, siendo eso {votosGanador} de votos")
else:
    print(f"Hay segunda vuelta, el primer partido es {partido1} con un {porcentajePartido1}% de votos, siendo eso {votosPartido1} de votos")
    print(f"El segundo partido es {partido2} con un {porcentajePartido2}% de votos, siendo eso {votosPartido2} de votos")
