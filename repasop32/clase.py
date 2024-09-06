class Trabajo:
    def __init__(self, nid=0, desc='', ttr=0, impt=0.0, cpa=0):
        self.numeroid = nid
        self.descripcion = desc
        self.tipotrabajo = ttr
        self.importe = impt
        self.personalafectado = cpa
    
    def __str__(self):
        return f'N° id: {self.numeroid} - Descripción: {self.descripcion} - Tipo de trabajo: {self.tipotrabajo} - Importe: {self.importe}$ - Personal afectado: {self.personalafectado}'
    