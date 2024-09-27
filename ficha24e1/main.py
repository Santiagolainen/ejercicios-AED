import clase

def search(v, x):
    for vec in v:
        if vec.codigo == x:
            return True
    
    return False


def validate_range(inf, sup, msg):
    n = int(input(msg))

    while n < inf or n > sup:
        print(f'Error, se solicitó un número en el rango [{inf}-{sup}]')
        n = int(input(msg))
    
    return n


def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))

        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')
    
    return n


def cont_ser(v):
    cont = [0] * 4

    for i in range(len(v)):
        cont[v[i].tiposervicio] += v[i].monto
    
    return cont


def find_max(v):
    max = 0
    im = None

    for i in range(len(v)):
        if im is None or v[i] > max:
            max = v[i]
            im = i
    
    return im


def crear_vector(v, x, cantas):
    new_v = []
    for i in range(len(v)):
        if v[i].edad > x and v[i].cantidadinvitados > cantas:
            new_v.append(v[i])
    
    return new_v

def main():
    op = -1
    fn = 'ficha24e1/reservas.csv'
    v = clase.carga(fn)

    while op != 5:
        print('Menu de opciones')
        print('='*120)
        print('1) Mostrar vector')
        print('2) Agregar reserva')
        print('3) Mostrar monto')
        print('4) Crear nuevo vector')
        print('5) Salir')
        op = int(input())
        print()

        if op == 1:
            if v:
                clase.display(v)
            else:
                print('El archivo no existe')
            print()
        elif op == 2:
            if v:
                cod = input('Ingrese el número de reserva: ')
                existe = search(v, cod)

                if existe:
                    print('Esa reserva ya existe')
                else:
                    nom = input('Ingrese el nombre: ')
                    ed = validate_range(0, 13, 'Ingrese la edad: ')
                    tipos = validate_range(0, 3, 'Ingrese el tipo de servicio: ')
                    canti = validate(0, 'Ingrese la cantidad de invitados: ')
                    mont = float(input('Ingrese el monto total: '))

                    v.append(clase.Reserva(cod, nom, ed, tipos, canti, mont))
            else:
                print('El archivo no existe')
            
            print()

        elif op == 3:
            if v:
                servicios = ('salón', 'salón y animación', 'salón, animación y comida niños', 'salón, animación, comida niños y sorpresitas')
                cont = cont_ser(v)

                for i in range(len(cont)):
                    print(f'El monto total del servicio "{servicios[i]}" es: {round(cont[i],2)}$')
                
                imax = find_max(cont)
                print()
                print(f'El servicio con el mayor monto es: {servicios[imax]}') 
            else:
                print('El archivo no existe')
            print()
        elif op == 4:
            if v:
                x = validate_range(0, 13, 'Ingrese la edad del cumpleañero: ')
                cantas = validate(0, 'Ingrese la cantidad de asistentes: ')

                nuevo_v = crear_vector(v, x, cantas)

                clase.display(nuevo_v)
            else:
                print('El archivo no existe')
            print()
        
        elif op == 5:
            if v:
                m = open(fn, 'wt')
                for i in range(len(v)):
                    m.write(f'{v[i].codigo},{v[i].nombre},{v[i].edad},{v[i].tiposervicio},{v[i].cantidadinvitados},{v[i].monto}\n')
                
                m.close()
            else:
                print('El archivo no existe')
            print()
    
    print('Programa finalizado...')


if __name__ == '__main__':
    main()