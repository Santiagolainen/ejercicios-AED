from encodings.utf_7 import encode


def validate(inf):
    k = inf

    while k <= inf:
        k = int(input(f'Ingrese un valor mayor a {k}: '))
        if k <= inf:
            print(f'Error, el valor debe ser mayor a {inf}')

    return k


def check(msg, abc):
    if msg is None or msg == '':
        return False

    for i in range(len(msg)):
        if msg[i] != ' ' and msg[i] not in abc:
            return False

    return True



def code_cesar(msg, abc, k):

    if not check(msg, abc):
        return None

    n = len(abc)
    b = []
    for i in range(len(msg)):
        if msg[i] == ' ':
            b.append(' ')

        else:
            im = abc.find(msg[i])

            ir = (im + k) % n

            b.append(abc[ir])

    encr = ''.join(b)
    return encr


def decode_cesar(msg, abc, k):
    if not check(msg, abc):
        return None

    n = len(abc)
    b = []

    for i in range(len(msg)):
        if msg[i] == ' ':
            b.append(' ')

        else:
            im = abc.find(msg[i])

            ir = (im - k + n) % n

            b.append(abc[ir])
    mens = ''.join(b)

    return mens


def code_trans(msg, abc, trans):
    if not check(msg, abc):
        return False

    b = []

    for i in range(len(msg)):
        if msg[i] == ' ':
            b.append(' ')

        else:
            im = abc.find(msg[i])

            b.append(trans[im])

    mens = ''.join(b)
    return mens



def decode_trans(msg, abc, trans):
    if not check(msg, abc):
        return None

    b = []

    for i in range(len(msg)):
        if msg[i] == ' ':
            b.append(' ')

        else:
            im = trans.find(msg[i])

            b.append(abc[im])

    mens = ''.join(b)
    return mens

def main():
    msg = input('Ingrese un mensaje para encriptar (solo mayusculas y espacios blancos): ')
    k = validate(0)
    abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    trans = "RISQPANOWXUMDHZTFGBLEYKCJVÑ"

    msg_encriptado_c = code_cesar(msg, abc, k)
    msg_desencriptado_c = decode_cesar(msg_encriptado_c, abc, k)
    msg_encriptado_t = code_trans(msg, abc, trans)
    msg_desencriptado_t = decode_trans(msg_encriptado_t, abc, trans)
    if msg_desencriptado_c is not None:
        print(f'Mensaje original: {msg}')
        print(f'Mensaje encriptado por la téncica de cesar: {msg_encriptado_c}')
        print(f'Mensaje desencriptado por la técninca de cesar es: {msg_desencriptado_c}')
    else:
        print('Error')
    if msg_desencriptado_t is not None:
        print(f'Mensaje original: {msg}')
        print(f'Mensaje encriptado por transposición: {msg_encriptado_t}')
        print(f'Mensaje desencriptado por transposición: {msg_desencriptado_t}')

if __name__ == '__main__':
    main()