import random

def verificacion_datos(token):
    mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    nums = '1234567890'
    valido = False
    cont_mayusculas = 0
    cont_nums = 0
    numeral = False
    for i in range(len(token)):
        if token[i] in mayusculas:
            cont_mayusculas += 1
        if token[i] in nums:
            cont_nums += 1
        if i > len(token)/2:
            if token[i] == '#':
                numeral = True
    if cont_mayusculas == 2 and cont_nums >= 2 and numeral == True:
        valido = True
    return valido
        
def operaciones_bancarias(num_operaciones):
    operaciones = []
    for i in range(num_operaciones):
        emp_part = random.choice(['Empresa', 'Particular'])
        monto_operado = random.randint(1, 99)
        peso_dolar = random.choice(['Pesos', 'Dolares'])
        operaciones.append([emp_part, monto_operado, peso_dolar])
    return operaciones

def por_op_dolares(operaciones):
    cont_op_dolares = 0
    for i in range(len(operaciones)):
        if operaciones[i][2] == 'Dolares':
            cont_op_dolares += 1
    porcentaje = (cont_op_dolares*100)/len(operaciones)
    return porcentaje

def monto_total_pesos(operaciones):
    suma_pesos = 0
    for i in range(len(operaciones)):
        if operaciones[i][0] == 'Particular' and operaciones[i][2] == 'Pesos':
            suma_pesos += operaciones[i][1]
    
    return suma_pesos

def monto_promedio_pesos(operaciones):
    cont_op_pesos = 0
    suma_pesos = 0
    promedio = 0
    for i in range(len(operaciones)):
        if operaciones[i][0] == 'Empresa' and operaciones[i][2] == 'Pesos':
            cont_op_pesos += 1
            suma_pesos += operaciones[i][1]
    if cont_op_pesos != 0:
        promedio = suma_pesos/cont_op_pesos
    return promedio



def main():
    verificacion = verificacion_datos('3K3mnsJklm#sn')
    if verificacion == True:
        op_bancarias = int(input('Ingrese la cantidad de operaciones bancarias realizadas: '))
        operaciones = operaciones_bancarias(op_bancarias)
        porcentaje = por_op_dolares(operaciones)
        suma_pesos = monto_total_pesos(operaciones)
        promedio_pesos = monto_promedio_pesos(operaciones)
        print('Menú de opciones')
        print('='*120)
        print('Seleccione que quiere saber')
        print('1 - Cantidad de operaciones bancarias\t\t\t\t 2 - Porcentaje de operaciones en dólares')
        print('3 - Monto total operado en pesos por particulares \t\t 4 - Monto promedio operado en pesos por las empresas')
        print('5 - Salir')
        op = int(input())
        while op != 5:
            if op == 1:
                print(f'\n\nSe llevaron a cabo {op_bancarias} operaciones bancarias\n\n')
                print('Menú de opciones')
                print('='*120)
                print('Seleccione que quiere saber')
                print('1 - Cantidad de operaciones bancarias\t\t\t\t 2 - Porcentaje de operaciones en dólares')
                print('3 - Monto total operado en pesos por particulares \t\t 4 - Monto promedio operado en pesos por las empresas')
                print('5 - Salir')
                op = int(input())
            elif op == 2:
                print(f'\n\nEl porcentaje de operaciones en dolares fue de un {porcentaje}%\n\n')
                print('Menú de opciones')
                print('='*120)
                print('Seleccione que quiere saber')
                print('1 - Cantidad de operaciones bancarias\t\t\t\t 2 - Porcentaje de operaciones en dólares')
                print('3 - Monto total operado en pesos por particulares \t\t 4 - Monto promedio operado en pesos por las empresas')
                print('5 - Salir')
                op = int(input())
            elif op == 3:
                print(f'\n\nEl monto total operado en pesos por particulares fue de {suma_pesos} pesos\n\n')
                print('Menú de opciones')
                print('='*120)
                print('Seleccione que quiere saber')
                print('1 - Cantidad de operaciones bancarias\t\t\t\t 2 - Porcentaje de operaciones en dólares')
                print('3 - Monto total operado en pesos por particulares \t\t 4 - Monto promedio operado en pesos por las empresas')
                print('5 - Salir')
                op = int(input())
            elif op == 4:
                print(f'\n\nEl monto promedio operado en pesos por las empresas fue de {promedio_pesos} pesos\n\n')
                print('Menú de opciones')
                print('='*120)
                print('Seleccione que quiere saber')
                print('1 - Cantidad de operaciones bancarias\t\t\t\t 2 - Porcentaje de operaciones en dólares')
                print('3 - Monto total operado en pesos por particulares \t\t 4 - Monto promedio operado en pesos por las empresas')
                print('5 - Salir')
                op = int(input())
            else:
                print('\n\nOpción no válida\n\n')
                print('Menú de opciones')
                print('='*120)
                print('Seleccione que quiere saber')
                print('1 - Cantidad de operaciones bancarias\t\t\t\t 2 - Porcentaje de operaciones en dólares')
                print('3 - Monto total operado en pesos por particulares \t\t 4 - Monto promedio operado en pesos por las empresas')
                print('5 - Salir')
                op = int(input())
    else:
        print('Token no válido')
    print('\nPrograma finalizado')

main()