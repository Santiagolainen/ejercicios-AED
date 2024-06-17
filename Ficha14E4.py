import random

def tiempo_salida():
    eleccion = random.randint(1,3)
    tiempo = 0
    while eleccion != 3:
        if eleccion == 1:
            tiempo += 3
        else:
            tiempo += 5
        eleccion = random.randint(1,3)
    tiempo += 7
    return tiempo

def main():
    tiempo = tiempo_salida()

    print(f'Tiempo: {tiempo} minutos')


if __name__ == '__main__':
    main()