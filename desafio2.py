__author__ = "Santiago"

n = int(input("Ingrese un número para calcular sus valores de órbita: "))
n_inicial = n
cont_orbita = 1
suma_n = 1
max_num = 0
orbita = []

while n != 1:

    if n > max_num:
        max_num = n
    
    if n % 2 == 0:
        orbita.append(n)
        cont_orbita += 1
        suma_n += n
        n = n/2
    else:
        orbita.append(n)
        cont_orbita += 1
        suma_n += n
        n = 3*n +1

promedio = suma_n/cont_orbita

orbita.append(1)
print(f"n = {n_inicial}")
print(f"Orbita de n = {n_inicial}: {orbita}")
print(f"Longitud de la órbita: {cont_orbita}")
print(f"Promedio de todos los valores de la órbita: {promedio}")
print(f"Mayor de los números de esa órbita: {max_num}")
