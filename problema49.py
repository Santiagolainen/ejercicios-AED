import random

class Socios:
    def __init__(self, nid, nom, aran, cod):
        self.numeroid = nid
        self.nombre = nom
        self.arancel = aran
        self.codigo = cod

    def __str__(self):
        return (f'N° de identificación: {self.numeroid} - Nombre: {self.nombre} - Arancel: {self.arancel} - '
                f'Código: {self.codigo}')


def validate(inf):
    n = inf

    while n <= inf:
        n = int(input())
        if n <= inf:
            print(f'Error, se solicita un valor mayor a {inf}')

    return n


def validate_code():
    code = int(input('Ingrese el código de deporte(0 - 9): '))

    while code > 9 or code < 0:
        print('Error, código no válido')
        code = int(input())

    return code


def carga(n):
    v_socios = []

    for i in range(n):
        nid = int(input('Ingrese el número de identificación: '))
        nom = input('Ingrese el nombre del socio: ')
        aran = float(input('Ingrese el arancel que paga cada mes: '))
        code = validate_code()
        v_socios.append(Socios(nid, nom, aran, code))

    return v_socios


def carga_random(n):
    v_socios = []
    nombres = ('Pepe', 'Pedro', 'Juan', 'Luis', 'Santiago', 'Marto', 'Tahhan', 'Gaston', 'Augusto')
    for i in range(n):
        nid = random.randint(1000, 10000)
        nom = random.choice(nombres)
        aran = random.randint(2000, 8000)
        code = random.randint(0, 9)

        v_socios.append(Socios(nid, nom, aran, code))

    return v_socios


def display(v):
    for i in range(len(v)):
        print(v[i])


def display_deportes(v):
    for i in range(len(v)):
        if v[i] > 0:
            print(f'La cantidad de socios que practican el deporte {i} son: {v[i]}')


def socios_deportes(v_socios):
    deportes = [0] * 10

    for i in range(len(v_socios)):
        deportes[v_socios[i].codigo] += 1

    return deportes


def sort(v):
    n = len(v)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].numeroid > v[j].numeroid:
                v[i], v[j] = v[j], v[i]


def buscar_aumentar_socio(nom_socio, v):
    for i in range(len(v)):
        if v[i].nombre == nom_socio:
            v[i].arancel += 100
            return v[i]
    return -1


def main():
    print('Ingrese la cantidad de socios: ')
    n = validate(0)

    op = -1
    while op != 0:
        print('Menu de opciones')
        print('=' * 160)
        print('1) Cargar arreglo con los datos de los socios')
        print('2) Mostrar datos de socios que paguen un arancel mayor a un valor dado')
        print('3) Mostrar la cantidad de socios que participan de cada deporte')
        print('4) Mostrar todos los datos ordenados de menor a mayor por número de identificación')
        print('5) Sumarle 100 pesos a un socio ingresado por teclado y mostrar sus datos')
        print('0) Salir')
        op = int(input())

        if op == 1:
            v_socios = carga_random(n)
            display(v_socios)
        elif op == 2:
            print('Ingrese el valor del arancel: ')
            p = validate(0)
            for i in range(len(v_socios)):
                if v_socios[i].arancel > p:
                    print(v_socios[i])
        elif op == 3:
            deportes = socios_deportes(v_socios)
            display_deportes(deportes)
        elif op == 4:
            sort(v_socios)
            display(v_socios)
        elif op == 5:
            nom_socio = input('Ingrese el nombre del socio que desea sumarle 100 pesos a su arancel: ')
            socio = buscar_aumentar_socio(nom_socio, v_socios)
            if socio != -1:
                print(socio)
            else:
                print('No hay ningún socio con ese nombre')

    print('Programa finalizado...')


if __name__ == '__main__':
    main()