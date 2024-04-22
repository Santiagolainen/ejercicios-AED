__author__ = "Santiago"


def orden_partidos(partidos):
    for i in range(len(partidos)):
        for j in range(len(partidos) - 1 - i):
            if partidos[j][1] < partidos[j + 1][1]:
                partidos[j], partidos[j + 1] = partidos[j + 1], partidos[j]
    return partidos


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
partidos_ordenados = orden_partidos(votPartidos)

if partidos_ordenados[0][2] > 45:
    b = 1
    partidoGanador = partidos_ordenados[0][0]
    votosGanador = partidos_ordenados[0][1]
    porcentajeGanador = partidos_ordenados[0][2]
else:
    partido1 = partidos_ordenados[0][0]
    votosPartido1 = partidos_ordenados[0][1]
    porcentajePartido1 = partidos_ordenados[0][2]
    partido2 = partidos_ordenados[1][0]
    votosPartido2 = partidos_ordenados[1][1]
    porcentajePartido2 = partidos_ordenados[1][2]

if b == 1:
    print(
        f"El partido {partidoGanador} ganó en primera vuelta con un {porcentajeGanador}% de votos, siendo eso {votosGanador} de votos")
else:
    print(
        f"Hay segunda vuelta, el primer partido es {partido1} con un {porcentajePartido1}% de votos, siendo eso {votosPartido1} de votos")
    print(
        f"El segundo partido es {partido2} con un {porcentajePartido2}% de votos, siendo eso {votosPartido2} de votos")

print(orden_partidos(votPartidos))
