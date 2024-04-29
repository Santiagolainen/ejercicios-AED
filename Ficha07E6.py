__author__ = "Santiago"

n = int(input("Ingrese la cantidad de puntos en el plano que desea saber: "))
coordenadas = []
cuadrante = 0
cuadrante1_3 = 0
distancia_origen = 0
distancia_origen_max = 0

cuadrantes = {0: "ningun cuadrante",
              1: "primer cuadrante",
              2: "segundo cuadrante",
              3: "tercer cuadrante",
              4: "cuarto cuadrante"}

for i in range(n):
    x = int(input("Ingrese la coordenada x: "))
    y = int(input("Ingrese la coordenada y: "))
    
    if x > 0 and y > 0:
        cuadrante = 1
        cuadrante1_3 += 1
    elif x < 0 and y > 0:
        cuadrante = 2
    elif x < 0 and y < 0: 
        cuadrante = 3
        cuadrante1_3 += 1
    elif x > 0 and y < 0:
        cuadrante = 4
    distancia_origen = pow(x**2 + y**2,1/2)

    if distancia_origen > distancia_origen_max:
        distancia_origen_max, punto_max = distancia_origen, i+1

    coordeanda = [x, y, cuadrante]

    coordenadas.append(coordeanda)

print(coordenadas)
k = 0
for i in coordenadas:
    k += 1
    print(f"Las coordenadas del punto {k} son ({i[0]};{i[1]})\nSe encuentra en la {cuadrantes[i[2]]}\n")

print(f"El punto que se encuentra más lejos del origen es el punto {punto_max}")
print(f"\nLa cantidad de puntos que se encuentran en el primero o tercer cuadrante son {cuadrante1_3}")