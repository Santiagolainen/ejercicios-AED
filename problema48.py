import random
from pydoc import visiblename


class Pieza:
    def __init__(self, cod=0, nom='', val=0.0, cant=0):
        self.codigo = cod
        self.nombre = nom
        self.valor = val
        self.cantidad = cant

    def __str__(self):
        return '| Código: {:<15} | Nombre: {:<20} | Valor: {:<30} | Cantidad: {:<3}'.format(self.codigo, self.nombre, self.valor, self.cantidad)


def carga_random(n):

    v_insumos = []
    nombres = ('Hierro', 'Metal', 'Acero', 'Aluminio', 'Plastico', 'Tornillo')
    for i in range(n):
        code = random.randint(1, 20)
        nom = random.choice(nombres)
        val = random.randint(100, 5000)
        cant = random.randint(0, 20)

        v_insumos.append(Pieza(code, nom, val, cant))

    return v_insumos


def val_code():
    code = int(input('Ingrese el código de insumo (entre 1 y 20): '))
    while code > 20 or code < 1:
        print('Error, código de insumo no válido (rango entre 1 y 20)')
        code = int(input())

    return code


def carga(n):
    v_insumos = []
    for i in range(n):
        code = val_code()
        nom = input('Ingrese el nombre del insumo: ')
        val = float(input('Ingrese el valor del insumo: '))
        cant = int(input('Ingrese la cantidad del insumo: '))

        v_insumos.append(Pieza(code, nom, val, cant))

    return v_insumos


def validate(inf):
    n = inf

    while n <= inf:
        n = int(input())
        if n <= inf:
            print(f'Error, se solicita un valor mayor a {inf}')

    return n


def val_pieza(v_insumos):

    n = len(v_insumos)
    suma = 0

    for i in range(n):
        suma += v_insumos[i].valor * v_insumos[i].cantidad

    return suma


def insumos_x(v_insumos, x):
    n = len(v_insumos)
    v_insumos_x = []

    for i in range(n):
        if v_insumos[i].cantidad < x:
            v_insumos_x.append(v_insumos[i])

    return v_insumos_x


def sort(v_insumos_x):
    n = len(v_insumos_x)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if v_insumos_x[i].codigo > v_insumos_x[j].codigo:
                v_insumos_x[i], v_insumos_x[j] = v_insumos_x[j], v_insumos_x[i]


def display(v):
    for i in range(len(v)):
        print(v[i])



def change(v_insumos, c):
    n = len(v_insumos)
    print('Insumos modificados: ')
    for i in range(n):
        if v_insumos[i].cantidad == 0:
            v_insumos[i].cantidad = c
            print(v_insumos[i])



def buscar_insumo(v_insumos, code):
    n = len(v_insumos)

    for i in range(n):
        if v_insumos[i].codigo == code:
            return v_insumos[i]

    return -1

def main():
    print('Ingrese la cantidad de insumos de la pieza')
    n = validate(0)

    op = -1
    while op != 0:
        print('Menu de opciones')
        print('=' * 160)
        print('1) Cargar datos de la pieza')
        print('2) Mostrar el valor total de la pieza')
        print('3) Mostrar los insumos cuya cantidad sea menor a un valor elegido')
        print('4) Reemplazar los insumos 0 por un valor elegido')
        print('5) Mostrar insumo por código')
        print('0) Salir')
        op = int(input())
        if op == 1:
            v_insumos = carga_random(n)
            display(v_insumos)
        elif op == 2:
            print('Valor total de la pieza:')
            valor = val_pieza(v_insumos)
            print(f'{valor}$')
        elif op == 3:
            print('Ingrese la cantidad x: ')
            cant = validate(-1)
            v_insumos_x = insumos_x(v_insumos, cant)
            sort(v_insumos_x)
            display(v_insumos_x)
        elif op == 4:
            print('Ingrese el valor para reemplazar los 0: ')
            c = validate(0)
            change(v_insumos, c)
        elif op == 5:
            print('Ingrese el código del insumo que desea buscar: ')
            codigo = validate(0)
            producto = buscar_insumo(v_insumos, codigo)
            if producto != -1:
                print(producto)
            else:
                print('No se ha encontrado el insumo solicitado')

    print('Programa finalizado...')


if __name__ == '__main__':
    main()