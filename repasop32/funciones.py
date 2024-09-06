def display(v):
    for i in range(len(v)):
        print()
        print(v[i])

def validate(inf, msg):
    n = inf

    while n <= inf:
        n = int(input(msg))
        if n <= inf:
            print(f'Error, se solicitó un número mayor a {inf}')
    
    return n


def validate_range(a, b, msg=''):
    n = int(input(msg))

    while n < a or n > b:
        print(f'Error, se solicitó un número en el rango {a}-{b}')
        n = int(input(msg))
    
    return n