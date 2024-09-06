import random

class Consumo:
    def __init__(self, impe, impg, impa):
        self.importe_electricidad = impe
        self.importe_gas = impg
        self.importe_agua = impa
    
    def __str__(self):
        return f'Importe de electricidad: {self.importe_electricidad}$ - Importe de gas: {self.importe_gas}$ - Importe de agua: {self.importe_agua}$'


def validate(inf, msg):
    n = inf

    while n <= inf:

        n = int(input(msg))

        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')
    
    return n


def carga(v):
    for f in range(len(v)):
        for c in range(len(v[f])):
            impe = float(input(f'Ingrese el importe de electricidad de la propiedad {f} en el mes {c}: '))
            impg = float(input(f'Ingrese el importe de gas de la propiedad {f} en el mes {c}: '))
            impa = float(input(f'Ingrese el importe de agua de la propiedad {f} en el mes {c}: '))
            v[f][c] = Consumo(impe, impg, impa)


def carga_random(v):
    for f in range(len(v)):
        for c in range(len(v[f])):
            impe = random.randint(0, 2000)
            impg = random.randint(0, 2000)
            impa = random.randint(0, 2000)
            v[f][c] = Consumo(impe, impg, impa)


def display(v):
    for f in range(len(v)):
        print()
        print()
        print(f'Propiedad {f}')
        for c in range(len(v[f])):
            print()
            print(f'Mes {c}')
            print(v[f][c])


def gasto_por_propiedad(v):
    v_suma = [0] * len(v)

    for f in range(len(v)):
        for c in range(len(v[f])):
            v_suma[f] += v[f][c].importe_electricidad + v[f][c].importe_gas + v[f][c].importe_agua
    
    return v_suma


def gasto_por_mes(v):
    filas = len(v)
    columnas = len(v[0])
    
    v_suma = [0] * columnas

    for c in range(columnas):
        for f in range(filas):
            v_suma[c] += v[f][c].importe_electricidad + v[f][c].importe_gas + v[f][c].importe_agua
    
    return v_suma



def main():
    n = validate(0, 'Ingrese la cantidad de propiedades que desea cargar: ')

    cons = n * [0]
    for f in range(n):
        cons[f] = 3 * [0]
    
    carga_random(cons)
    display(cons)
    
    gasto_p_propiedad = gasto_por_propiedad(cons)
    gasto_p_mes = gasto_por_mes(cons)
    
    print()
    
    for i in range(len(gasto_p_propiedad)):
        print(f'El gasto de la propiedad {i} fue de: {gasto_p_propiedad[i]}$')
        print()

    for i in range(len(gasto_p_mes)):
        print(f'El gasto del mes {i} fue de: {gasto_p_mes[i]}$')
        print()



if __name__ == '__main__':
    main()