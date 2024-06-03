def leer_archivo(archivo):
    m = open(archivo)
    oracion = m.read()
    m.close()
    return oracion

def pal_car_dig(oracion):
    palabra_dig = False
    cont_pal_dig = 0
    nums = '1234567890'
    i = 0
    if '.' not in oracion:
        return 'Error'
    else:
        while oracion[i] != '.':
            if palabra_dig == False and oracion[i] in nums:
                palabra_dig = True
                cont_pal_dig += 1
            if oracion[i] == ' ':
                palabra_dig = False
            i += 1
    return cont_pal_dig


def pal_3_letras(oracion):
    palabra = ''
    cont_pal_3 = 0
    i = 0
    while oracion[i] != '.':
        if oracion[i] != ' ':
            palabra += oracion[i]
        else:
            if len(palabra) <= 3 and len(palabra) > 0:
                cont_pal_3 += 1
            palabra = ''
        i += 1
    if len(palabra) <= 3 and len(palabra) > 0:
        cont_pal_3 += 1
    return cont_pal_3

def pal_4_6_letras(oracion):
    palabra = ''
    cont_pal_4_6 = 0
    i = 0
    while oracion[i] != '.':
        if oracion[i] != ' ':
            palabra += oracion[i]
        else:
            if 4 <= len(palabra) <= 6 and len(palabra) > 0:
                cont_pal_4_6 += 1
            palabra = ''
        i += 1
    if 4 <= len(palabra) <= 6 and len(palabra) > 0:
        cont_pal_4_6 += 1
    return cont_pal_4_6

def pal_6_letras(oracion):
    palabra = ''
    cont_pal_6 = 0
    i = 0
    while oracion[i] != '.':
        if oracion[i] != ' ':
            palabra += oracion[i]
        else:
            if 6 < len(palabra)  and len(palabra) > 0:
                cont_pal_6 += 1
            palabra = ''
        i += 1
    if len(palabra) > 6 and len(palabra) > 0:
        cont_pal_6 += 1
    return cont_pal_6
            
def pal_larga(oracion):
    palabra_mas_larga = ''
    palabra = ''
    i = 0
    while oracion[i] != '.':
        if oracion[i] != ' ':
            palabra += oracion[i]
        else:
            if len(palabra) > len(palabra_mas_larga):
                palabra_mas_larga = palabra
            palabra = ''
        i += 1
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra
    return palabra_mas_larga

def exp_de(oracion):
    palabra = ''
    i = 0
    cont_pal_de = 0
    while oracion[i] != '.':
        if oracion[i] != ' ':
            palabra += oracion[i]
        else:
            mitad_palabra = len(palabra)//2 + 1
            if 'de' in palabra[0: mitad_palabra]:
                cont_pal_de += 1
            palabra = ''
        i += 1
    if 'de' in palabra[0: mitad_palabra]:
                cont_pal_de += 1
    return cont_pal_de


def main():
    oracion = leer_archivo('palabras.txt')
    palabras_con_digito = pal_car_dig(oracion)
    palabras_3_letras = pal_3_letras(oracion)
    palabras_4_6_letras = pal_4_6_letras(oracion)
    palabras_6_letras = pal_6_letras(oracion)
    palabra_mas_larga = pal_larga(oracion)
    pal_de = exp_de(oracion)
    print(f'La cantidad de palabras que tenían al menos un caracter que era un dígito eran: {palabras_con_digito}')
    print(f'La cantidad de palabras con 3 letras o menos fueron: {palabras_3_letras}')
    print(f'La cantidad de palabras con 4 hasta 6 letras fueron: {palabras_4_6_letras}')
    print(f'La cantidad de palabras con más de 6 letras fueron: {palabras_6_letras}')
    print(f'La palabra más larga del texto fue "{palabra_mas_larga}"')
    print(f'La cantidad de palabras con la expresión "de" en la primera mitad son: {pal_de}')

main()