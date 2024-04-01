__author__ = "Santiago"

cantidadCandidatos = int(input("Ingrese la cantidad de candidatos: "))

candidatos = []

for i in range(cantidadCandidatos):
    apellido = input(f"Ingrese el apellido del candidato {i + 1}: ")
    nombre = input(f"Ingrese el nombre del candidato {i + 1}: ")
    votos = int(input(f"Ingrese la cantidad de votos del candidato {i + 1}: "))
    iniciales = apellido[0] + nombre[0]
    cantidadVotos = "x"*votos
    candidato = {"Iniciales": iniciales, "Votos": votos, "Cantidad de votos": cantidadVotos}
    candidatos.append(candidato)

for i, candidato in enumerate(candidatos):
    print(f"Candidato {i +1}:\nIniciales: {candidato['Iniciales']},\nCantidad de votos({candidato['Votos']}) \n{candidato['Cantidad de votos']}\n")
