import random

class Alumno:
    def __init__(self, nom, prom):
        self.nombre = nom
        self.promedio = prom
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Promedio: {self.promedio}'


def generate_random(v):
    nombres = ('Pedro', 'Raul', 'Tahhan', 'Gustavo', 'Augusto', 'Martin', 'Andrea', 'Mirta')

    for i in range(len(v)):
        nom = random.choice(nombres)
        prom = round(random.uniform(0, 10),2)

        v[i] = Alumno(nom, prom)


def display(v):
    for vec in v:
        print(vec)