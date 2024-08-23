import random


class Jugadores:
    def __init__(self, nom, num=0, pal='', pun=0):
        self.nombre = nom
        self.numero = num
        self.palo = pal
        self.puntos = pun

    def __str__(self):
        return f'Nombre: {self.nombre} - Número: {self.numero} - Palo: {self.palo}'



def ronda(j1, j2):
    if j1.numero > j2.numero:
        return j1
    elif j2.numero > j1.numero:
        return j2
    elif j1.numero == j2.numero:
        if j1.palo == 'Oro':
            return j1
        elif j2.palo == 'Oro':
            return j2
        else:
            return 0



def main():
    palos = ['Espada', 'Oro', 'Copa', 'Bastos']
    numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    j1 = Jugadores('Pepe')
    j2 = Jugadores('Raul')


    for i in range(3):
        j1.numero = random.choice(numeros)
        j1.palo = random.choice(palos)
        j2.numero = random.choice(numeros)
        j2.palo = random.choice(palos)

        r = ronda(j1, j2)
        print(j1)
        print(j2)
        print(r)
        if r != 0:
            if r == j1:
                j1.puntos += j1.numero
            elif r == j2:
                j2.puntos += j2.numero

    if j1.puntos > j2.puntos:
        print(f'El ganador fué {j1.nombre} con {j1.puntos} puntos contra {j2.puntos} de {j2.nombre}')
    elif j2.puntos > j1.puntos:
        print(f'El ganador fué {j2.nombre} con {j2.puntos} puntos contra {j1.puntos} de {j1.nombre}')
    else:
        print('No hubo ganador')




if __name__ == '__main__':
    main()