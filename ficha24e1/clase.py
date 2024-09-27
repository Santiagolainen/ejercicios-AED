import os

class Reserva:
    def __init__(self, cod='', nom='', ed=0, tipos=0, canti=0, mont=0.0):
        self.codigo = cod
        self.nombre = nom
        self.edad = ed
        self.tiposervicio = tipos
        self.cantidadinvitados = canti
        self.monto = mont
    
    def __str__(self):
        servicios = ('salón', 'salón y animación', 'salón, animación y comida niños', 'salón, animación, comida niños y sorpresitas')
        return (f'Número de reserva: {self.codigo} - Nombre: {self.nombre} - Edad: {self.edad} - '
                f'Tipo servicio: {servicios[self.tiposervicio]} - Cantidad invitados: {self.cantidadinvitados} - '
                f'Monto: {self.monto}$')


def carga(fn):

    v = []
    
    if os.path.exists(fn):
        m = open(fn, 'rt')
        while True:
            line = m.readline()
            
            if line == '':
                break
            
            if line[-1] == '\n':
                line = line[:-1]
            
            datos = line.split(',')
            
            cod = datos[0]
            nom = datos[1]
            ed = int(datos[2])
            tipos = int(datos[3])
            canti = int(datos[4])
            mont = float(datos[5])

            v.append(Reserva(cod, nom, ed, tipos, canti, mont))

        m.close()
        return v
    else:
        return

def display(v):
    for vec in v:
        print(vec)