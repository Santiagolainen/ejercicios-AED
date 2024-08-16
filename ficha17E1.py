import random

def carga(n, v_temp, v_reg, v_mes, regiones):

    for i in range(n):
        m = random.randint(-40, 50)
        v_temp.append(m)
        m = random.randint(1, 20)
        v_reg.append(m)
        regiones[m - 1] += 1
        m = random.randint(1, 31)
        v_mes.append(m)

def prom(v_temp):
    n = len(v_temp)
    suma = 0
    for i in range(n):
        suma += v_temp[i]
    
    if n > 0:
        return suma//n 
    
    return 0



def sort(v_temp, v_reg, v_mes):
    n = len(v_temp) 

    for i in range(n-1):
        for j in range(i + 1, n):
            if v_mes[i] > v_mes[j]:
                v_temp[i], v_temp[j] = v_temp[j], v_temp[i]
                v_reg[i], v_reg[j] = v_reg[j], v_reg[i]
                v_mes[i], v_mes[j] = v_mes[j], v_mes[i]



def mostrar_temp(region, v_temp, v_reg, v_mes):
    n = len(v_temp)

    for i in range(n):
        if v_reg[i] == region:
            print(f'Día: {v_mes[i]}\nTemperatura: {v_temp[i]}°')



def search(x, region, v_temp, v_reg):
    n = len(v_temp)

    for i in range(n):
        if v_reg[i] == region and v_temp[i] > x:
            return True
    
    return False


def mostrar_temp_reg(regiones):
    n = len(regiones)

    for i in range(n):
        if regiones[i] != 0:
            print(f'Muestras en la región {i+1}: {regiones[i]}')



def main():
    n = int(input('Ingrese cuantas temperaturas desea regsitrar: '))

    v_temp = []
    v_reg = []
    v_mes = []
    regiones = [0] * 20

    carga(n, v_temp, v_reg, v_mes, regiones)
    sort(v_temp, v_reg, v_mes)
    region = random.randint(1, 20)
    temp = int(input('Ingrese la temperatura a superar: '))
    supero_x = search(temp, region, v_temp, v_reg)
    promedio = prom(v_temp)
    print(f'El promedio general de temperatura fue de {promedio}°')
    print(f'Temperaturas de la región {region}: ')
    mostrar_temp(region, v_temp, v_reg, v_mes)
    

    if supero_x:
        print(f'Hay al menos un valor que superó a la temperatura {temp}° en la región {region}')
    else:
        print(f'Ninguna temperatura en la región {region} superó los {temp}°')
    
    mostrar_temp_reg(regiones)



if __name__ == '__main__':
    main()