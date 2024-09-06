import clase
import random
import funciones


def carga(n):
    v = []

    for i in range(n):
        nid = funciones.validate(0, 'Ingrese el número de identificación: ')
        desc = input('Ingrese la descripción del trabajo: ')
        ttr = funciones.validate_range(0, 19, 'Ingrese el tipo de servicio: ')
        imp = float(input('Ingrese el importe: '))
        cpa = int(input('Ingrese la cantidad de personal afectado: '))
        v.append(clase.Trabajo(nid, desc, ttr, imp, cpa))
    
    return v


def carga_random(n):
    v = []
    descs = ('Carga', 'Descarga', 'Avion', 'Auto', 'Motocross', 'Firulo')
    
    for i in range(n):

        nid = random.randint(1, 1000)
        desc = random.choice(descs)
        ttr = random.randint(0, 19)
        imp = random.randint(0, 5000)
        cpa = random.randint(0, 200)

        v.append(clase.Trabajo(nid, desc, ttr, imp, cpa))
    
    return v


def display_may_0(v):
    for i in range(len(v)):
        if v[i] > 0:
            print()
            print(f'Se ofrecen {v[i]} trabajos del tipo {i}')


def sort(v):
    n = len(v)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].numeroid < v[j].numeroid:
                v[i], v[j] = v[j], v[i]


def tpm3(v):
    v_p = []

    for i in range(len(v)):
        if v[i].personalafectado > 3:
            v_p.append(v[i])
    
    return v_p


def suma_imp(v):
    suma = 0

    for i in range(len(v)):
        suma += v[i].importe
    
    return suma


def tot_tipt(v):
    v_t = [0] * 20

    for i in range(len(v)):
        v_t[v[i].tipotrabajo] += 1
    
    return v_t


def search(num, t, v):
    for i in range(len(v)):
        if v[i].numeroid == num and v[i].tipotrabajo == t:
            return v[i]
    
    return -1


def main():
    n = funciones.validate(0, 'Ingrese la cantidad de trabajos que desea cargar en el arreglo: ')

    op = -1

    while op != 0:
        print()
        print('Menu de opciones')
        print('='*120)
        print('1) Cargar arreglo con los datos de los trabajos')
        print('2) Mostrar datos de los trabajos cuya cantidad de personal sea mayor a 3, '
              'ordenado de mayor a menor por n° de identificación mostrando la suma de los importes de los registros mostrados')
        print('3) Mostrar la cantidad de trabajos que se ofrecen de cada tipo')
        print('4) Mostrar datos de los trabajos cuyo importe sea mayor al importe promedio')
        print('5) Buscar trabajo por número de identificación y tipo de trabajo')
        print('0) Salir')
        print()

        op = int(input())

        if op == 1:
            v_trabajos = carga_random(n)
            funciones.display(v_trabajos)
        elif op == 2:
            v_tpm3 = tpm3(v_trabajos)
            total_imp = suma_imp(v_tpm3)
            sort(v_tpm3)
            print('Trabajos cuya cantidad de personal es mayor a 3:')
            funciones.display(v_tpm3)
            print()
            print(f'Suma de los importes de los registros mostrados: {total_imp}$')
        elif op == 3:
            cont_tt = tot_tipt(v_trabajos)
            display_may_0(cont_tt)
        elif op == 4:
            suma = suma_imp(v_trabajos)
            promedio = suma/len(v_trabajos)

            print('Trabajos cuyo importe es mayor al promedio')
            
            for i in range(len(v_trabajos)):
                if v_trabajos[i].importe > promedio:
                    print()
                    print(v_trabajos[i])

        elif op == 5:
            num = funciones.validate(0, 'Ingrese el número de identificación a buscar: ')
            t = funciones.validate_range(0, 19, 'Ingrese el tipo de trabajo a buscar: ')

            registro = search(num, t, v_trabajos)

            print()
            if registro != -1:
                print(registro)
            else:
                print('Error, no existe un trabajo con ese n° y tipo')
    
    print('Programa finalizado...')

if __name__ == '__main__':
    main()