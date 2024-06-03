def normalize(s):
    replacements = (('á', 'a'),('é', 'e'),('í', 'i'),('ó', 'o'),('ú', 'u'))
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def pal_3_vocales(texto):
    vocales = 'aeiou'
    i = 0
    palabra = ''
    cont_vocales = 0
    palabras_3_vocales = 0
    while texto[i] != '.':
        if texto[i] != ' ':
            palabra += texto[i]
        else:
            for j in palabra:
                if j in vocales:
                    cont_vocales += 1
            if cont_vocales == 3:
                palabras_3_vocales += 1
            palabra = ''
            cont_vocales = 0
        i += 1
    for j in palabra:
        if j in vocales:
            cont_vocales += 1
        if cont_vocales == 3:
            palabras_3_vocales += 1
    
    return palabras_3_vocales

def por_pal_dig(texto):
    nums = '1234567890'
    i = 0
    cont_pal_dig = 0
    palabra_digito = False
    cont_letras = 0
    palabras = 0
    porcentaje = 0

    while texto[i] != '.':
        if texto[i] != ' ':
            if texto[i] in nums:
                palabra_digito = True
            else:
                cont_letras += 1
        else:
            if palabra_digito == True and cont_letras > 4:
                cont_pal_dig += 1
            palabra_digito = False
            cont_letras = 0
            palabras += 1
        i += 1

    if palabra_digito == True and cont_letras > 4:
        cont_pal_dig += 1
    palabras += 1
    
    if palabras != 0:
        porcentaje = (cont_pal_dig*100)/palabras 
    return porcentaje

def pal_terminan_primera_letra(texto):
    texto = texto.strip().lower()
    texto = normalize(texto)
    palabra = ''
    primera_letra = texto[0]
    pal_men_car = None
    orden_pal_men_car = 0
    orden_palabras = 1
    i = 0
    while texto[i] != '.':
        if texto[i] != ' ':
            palabra += texto[i]
        else:
            if palabra[-1] == primera_letra:
                if pal_men_car == None:
                    pal_men_car = palabra
                if pal_men_car != None and len(palabra) < len(pal_men_car):
                    orden_pal_men_car = orden_palabras
                    pal_men_car = palabra
            orden_palabras += 1
            palabra = ''
        i += 1
    if palabra[-1] == primera_letra:
        if len(palabra) < len(pal_men_car):
            orden_pal_men_car = orden_palabras
            pal_men_car = palabra
        orden_palabras += 1
    return orden_pal_men_car

def pal_men(texto):
    palabra = ''
    i = 0
    cont_pal_men = 0
    while texto[i] != '.':
        if texto[i] != ' ':
            palabra += texto[i]
        else:
            mitad_palabra = len(palabra)//2 + 1 
            if 'men' in palabra[0: mitad_palabra]:
                cont_pal_men += 1
            palabra = ''
        i += 1
    mitad_palabra = len(palabra)//2 + 1 
    if 'men' in palabra[0: mitad_palabra]:
        cont_pal_men += 1
    
    return cont_pal_men

            



def main():
    texto = input('Ingrese un texto finalizado por un punto: ')
    palabras_3_vocales = pal_3_vocales(texto)
    porcentaje = por_pal_dig(texto)
    orden_palabra_menos_car = pal_terminan_primera_letra(texto)
    palabras_men = pal_men(texto)
    print(f'La cantidad de palabras que tuvieron exactamente 3 vocales fueron {palabras_3_vocales} palabras')
    print(f'El porcentaje de palabras que tuvieron algun dígito y más de 4 letras fue de un {porcentaje}%')
    print(f'La posición de la palabra con menos letras y que termina con la letra con la que empieza'
          f'la primera palabra es la posición número: {orden_palabra_menos_car}')
    print(f'La cantidad de palabras que contienen "men" son {palabras_men}')

main()