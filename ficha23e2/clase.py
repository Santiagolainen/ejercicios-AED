class Alquiler:
    def __init__(self, id='', mont=0.0, tipoc=0):
        self.dni = id
        self.monto = mont
        self.tipocabana = tipoc
    
    def __str__(self):
        return f'DNI: {self.dni} - Monto: {self.monto}$ - Tipo cabaña: {self.tipocabana}'

