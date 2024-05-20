__author__ = "Santiago"

def pal_4_letras(palabra):
    palabra_split = palabra.split()
    i = 0
    cont_pal_4 = 0

    if "." not in palabra:
        cont_pal_4 = 0
    else:
        if len(palabra_split) != 0:
            while "." not in palabra_split[i]:
                if len(palabra_split[i]) > 4:
                    cont_pal_4 += 1
                i += 1
            if len(palabra_split[i]) > 4:
                cont_pal_4 += 1
        else:
            cont_pal_4 = 0
    
    return cont_pal_4

def x_y(palabra):
    palabra_split = palabra.split()
    i = 0
    cont_x_y = 0
    if "." not in palabra:
        cont_x_y = 0
    else:
        if len(palabra_split) != 0:
            while "." not in palabra_split[i]:
                if "x" in palabra_split[i] or "y" in palabra_split[i]:
                    cont_x_y += 1
                i += 1
            if "x" in palabra_split[i] or "y" in palabra_split[i]:
                cont_x_y += 1
        else:
            cont_x_y = 0
    
    return cont_x_y

def promedio_letras(oracion):
    cont_letras = 0
    cont_palabras = 0
    promedio = 0
    palabras = oracion.split()
    if "." not in oracion:
        promedio = 0
    else:
        if len(oracion) != 0:
            j = 0
            while "." not in palabras[j]:
                cont_palabras += 1
                j += 1
            cont_palabras += 1
            i = 0
            while oracion[i] != ".":
                if oracion[i] != " ":
                    cont_letras += 1
                else:
                    i += 1
                    continue
                i += 1
            promedio = cont_letras/cont_palabras
        else:
            promedio = 0
    
    return round(promedio,2)

def pal_mo(oracion):
    cont_pal_mo = 0
    oracion = oracion.lower()
    if "." not in oracion:
        cont_pal_mo = 0
    else:
        if len(oracion) != 0:
            b_palabra = True
            cont_pal_mo = 0
            for i in range(len(oracion) - 1):
                letra_posterior = oracion[i + 1]
                if i == 0:
                    if oracion[i] == "m" and letra_posterior == "o":
                        cont_pal_mo += 1
                        b_palabra = False
                else:
                    if oracion == " " and letra_posterior != " ":
                        b_palabra = True
                    if b_palabra == True:
                        if oracion[i] == "m" and letra_posterior == "o":
                            cont_pal_mo += 1
                            b_palabra = False
        else:
            cont_pal_mo = 0


    return cont_pal_mo
        


oracion = input("Ingrese una palabra finalizada con un punto: ")
print(f"Palabras con más de 4 letras: {pal_4_letras(oracion)}")
print(f"Palabras que tenían al menos una vez la letra \"x\" o \"y\": {x_y(oracion)}")
print(f"El promedio de letras por palabra en todo el texto es: {promedio_letras(oracion)}")
print(f"Las palabras que contuvieron sólo una vez la expresion \"mo\" fueron {pal_mo(oracion)} palabras")