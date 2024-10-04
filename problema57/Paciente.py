class Paciente:
    def __init__(self, cod=0, nom='', fech=0, code=0):
        self.codigo = cod
        self.nombre = nom
        self.fecha = fech
        self.codigoenfermedad = code

    def __str__(self):
        return (f'N° Historia clínica: {self.codigo} - Nombre: {self.nombre} - Fecha última visita: {self.fecha} - '
                f'Código enfermedad: {self.codigoenfermedad}')

