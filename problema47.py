class Estudiante:
    def __init__(self, leg=0, nom='', prom=0.0):
        self.legajo = leg
        self.nombre = nom
        self.promedio = prom

    def __str__(self):
        return f'Legajo: {self.legajo} - Nombre: {self.nombre} - Promedio: {self.promedio}'


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input(f'Ingrese una cantidad mayor a {inf}: '))
        if n <= inf:
            print(f'Error, se pidió mayor a {inf}')
    return n



def carga(n):
    v = []
    for i in range(n):
        leg = int(input('Ingrese el legajo: '))
        nom = input('Ingrese el nombre: ')
        prom = float(input('Ingrese el promedio: '))
        v.append(Estudiante(leg, nom, prom))

    return v



def prom_may_x(prom, v_alumnos):
    v_a_in = []
    for i in range(len(v_alumnos)):
        if v_alumnos[i].promedio >= prom:
            v_a_in.append(v_alumnos[i])

    return v_a_in



def sort(v_a_in):
    n = len(v_a_in)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if v_a_in[i].legajo > v_a_in[j].legajo:
                v_a_in[i], v_a_in[j] = v_a_in[j], v_a_in[i]



def main():
    n = validate(0)

    v_alumnos = carga(n)
    prom = float(input('Ingrese el promedio que se debe superar para ingresar al curso: '))
    v_a_in = prom_may_x(prom, v_alumnos)
    sort(v_a_in)

    for i in range(len(v_a_in)):
        print(v_a_in[i])


if __name__ == '__main__':
    main()