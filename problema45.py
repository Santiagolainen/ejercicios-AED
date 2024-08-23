import math


class Point:
    pass


def init(cx, cy):
    p = Point()
    p.x = cx
    p.y = cy
    return p

def to_string(p):
    return f'(x: {p.x}; y: {p.y})'

def main():
    op = -1
    while op != 4:
        print('Menu de opciones')
        print('='*160)
        print('1 - Cargar datos de un punto y mostrar\t\t\t\t\t\t\t\t\t\t\t 2 - Cargar datos de un punto y mostrar distancia al'
              ' origen desde ese punto')
        print('3 - Cargar datos de un punto y mostrar la pendiente de la recta que los une \t 4 - Salir')
        op = int(input())
        if op == 1:
            p1 = init(float(input('Ingrese el valor para x: ')), float(input('Ingrese el valor para y: ')))
            print(to_string(p1))
        elif op == 2:
            p1 = init(float(input('Ingrese el valor para x: ')), float(input('Ingrese el valor para y: ')))
            dist_or = math.sqrt(p1.x**2 + p1.y**2)
            print(f'La distancia al origen es {dist_or}')
        elif op == 3:
            p1 = init(float(input('Ingrese el valor para x: ')), float(input('Ingrese el valor para y: ')))
            if p1.x != 0:
                m = p1.y / p1.x
            else:
                m = 0
            print(f'La pendiente de la recta es {m}')
        elif op > 4:
            print('Número no válido')
            op = int(input('Ingrese una opción: '))


    print('Finalizando programa... NDEAAAAAAAAAAAAAHHHHHH')

if __name__ == '__main__':
    main()