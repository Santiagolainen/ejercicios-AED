class Atletas:
    def __init__(self, nom, t_nat, t_cicl, t_corr):
        self.nombre = nom
        self.t_natacion = t_nat
        self.t_ciclismo = t_cicl
        self.t_corriendo = t_corr
    
    def prom(self):
        return (self.t_natacion + self.t_ciclismo + self.t_corriendo) / 3
    
    def __str__(self):
        return f'{self.nombre}, Promedio: {self.prom()}'
    
    def __repr__(self):
        return f'Atletas(nombre={self.nombre}, prom={self.prom():.2f})'


def sort_v(v):
    for i in range(0, len(v) - 1):
        for j in range(i + 1, len(v)):
            if v[i].prom() < v[j].prom():
                v[i], v[j] = v[j], v[i]


def main():
    at1 = Atletas('Pepe', 30, 40, 120)
    at2 = Atletas('Raul', 20, 32, 200)
    at3 = Atletas('Jorge', 80, 15, 90)

    atletas = [at1, at2, at3]
    sort_v(atletas)

    print(atletas.__str__())

    for i in range(len(atletas)):
        print(f'El puesto {i+1} es para {atletas[i].nombre} con un promedio de {round(atletas[i].prom(),2)}')




if __name__ == '__main__':
    main()