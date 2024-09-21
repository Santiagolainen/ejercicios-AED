import random

class Libro:
    def __init__(self, cod, tit, aut):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut

    def __str__(self):
        return f'ISBN: {self.isbn} - Título: {self.titulo} - Autor: {self.autor}'


def generate_random(v):
    titulos = ('Leon el rey', 'Pocajontas', 'La cenicienta', 'La princesa y los siete enantios', 'Rapunzel',
               'Bambi', 'Red')
    autores = ('Pepe', 'Marcelo', 'Roberto', 'Gallardo', 'Luis', 'Enrique', 'Rodolfo', 'Josefa', 'Maria')

    for i in range(len(v)):
        cod = random.randint(100,999)
        tit = random.choice(titulos)
        aut = random.choice(autores)

        v[i] = Libro(cod, tit, aut)

def display(v):
    for vec in v:
        print(vec)