import os

class Reserva:
    def __init__(self, cod='', nom='', cantp=0, tipor=0, mont=0.0, cantd=0):
        self.codigo = cod
        self.nombre = nom
        self.cantpersonas = cantp
        self.tiporesidencia = tipor
        self.monto = mont
        self.cantdias = cantd
    
    def __str__(self):
        residencias = ('Departamento', 'Cabaña', 'Hotel Spa', 'Casa', 'Chalet', 'Hostería')
        return (f'Número de reserva: {self.codigo} - Nombre: {self.nombre} - Cantidad de personas: {self.cantpersonas} - '
                f'Tipo de residencia: {residencias[self.tiporesidencia]} - Monto por día: {self.monto}$ - Cantidad de días: {self.cantdias}')
    
def display(v):
    for vec in v:
        print(vec)

def generate(fn):
    v = []
    
    if os.path.exists(fn):

        m = open(fn, 'rt')
        m.readline()
        while True:
            line = m.readline()

            if line == '':
                break

            datos = line.split(',')

            v.append(Reserva(datos[0], datos[1], int(datos[2]), int(datos[3]), float(datos[4]), int(datos[5])))
        
        m.close()

    return v