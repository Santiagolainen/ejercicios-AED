class Votante:
    def __init__(self, cod, nom, ed, sex):
        self.dni = cod
        self.nombre = nom
        self.edad = ed
        self.sexo = sex

    def __str__(self):
        return f'DNI: {self.dni} - Nombre: {self.nombre} - Edad: {self.edad} - Sexo: {self.sexo}'