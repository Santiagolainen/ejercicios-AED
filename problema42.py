def validate(inf):
    n = inf
    while n <= inf:
        n = int(input(f'Ingrese un valor mayor a {inf}: '))
        if n <= inf:
            print(f'Error, el valor debe ser mayor a {inf}')

    return n


def carga(n):
    v = []

    for i in range(n):
        v.append(int(input(f'Ingrese un número entero: ')))

    return v



def merge(v_n, v_m):
    v_3 = []

    for i in range(len(v_n)):

        exists = False

        for k in range(len(v_3)):
            if v_3[k] == v_n[i]:
                exists = True
                break
        if not exists:
            for j in range(len(v_m)):
                if v_n[i] == v_m[j]:
                    v_3.append(v_n[i])
                    break

    return v_3

def main():
    n = validate(0)
    v_n = carga(n)

    m = validate(0)
    v_m = carga(m)

    v_3 = merge(v_n, v_m)

    print(v_3)


if __name__ == '__main__':
    main()