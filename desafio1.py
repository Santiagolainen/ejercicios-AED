__author__ = "Santiago"

# Pregunto que operación el usuario quiere hacer
operacion = input("Escriba \"h\" si desea realizar una conversion de segundos a HH:MM:SS o \"s\" si desea realizar una conversión de HH:MM:SS a segundos: ")

# Compruebo que operación decidio realizar con un if
if operacion == "h":
    # Ingreso de segundos para la primera parte del desafio
    segundos = int(input("Ingrese la cantidad de segundos: "))
    # Compruebo si son más de 24 horas
    if segundos//3600 < 25:

        # Asignación vacia de todas las variables que voy a usar
        horas = 0
        minutos = 0
        sec = 0

        if segundos > 3600:
            horas = segundos // 3600

        if segundos > 60:
            minutos = (segundos % 3600) // 60

        # Asigno una variable nueva para los segundos que voy a mostrar en pantalla para evitar cualquier confusión o error de código
        sec = (segundos % 3600) % 60

        # Muestro el resultado final
        print(f"Cantidad de horas, minutos y segudnos: {horas}:{minutos}:{sec}")
    else:
        print("Excedido")
elif operacion == "s":
    # Ingreso por teclado las variables para resolver la segunda parte del problema
    # Pongo un 2 en cada variable nueva para dejar en claro que esto es de la segunda parte del problema y evitar confusiones y/o
    # problemas con las variables anteriores
    horas2 = int(input("Ingrese la cantidad de horas: "))
    minutos2 = int(input("Ingrese la cantidad de minutos: "))
    segundos2 = int(input("Ingrese la cantidad de segundos: "))

    # calculo los segundos multiplicando las horas por 3600 (cantidad de segundos en una hora), los minutos por 60 y sumando la cantidad de segundos
    segundosTotal = horas2*3600 + minutos2*60 + segundos2

    # Muestro los segundos en total
    print("La cantidad de segundos total es de:", segundosTotal)
# Uso este else por si ingresa un valor que es distinto de h o s
else:
    print("No es una operación válida")




