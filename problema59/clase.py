class Articulo:
    def __init__(self, cod=0, tit='', cp=0, ta=0, idio=0):
        self.codigo = cod
        self.titulo = tit
        self.cantpag = cp
        self.tipoarticulo = ta
        self.idioma = idio

    def __str__(self):
        return (f'Código: {self.codigo} - Titulo: {self.titulo} - Cantidad de páginas: {self.cantpag} - '
                f'Tipo de artículo: {self.tipoarticulo} - Idioma: {self.idioma}')