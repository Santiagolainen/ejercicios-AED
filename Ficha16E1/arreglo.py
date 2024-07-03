import random

def array(n):
    vec = []
    for i in range(n):
        num = random.randint(1, 100)
        vec.append(num)
    return vec

def ord_asc(vec):
    for i in range(len(vec) - 1):
        for j in range(i + 1, len(vec)):
            if vec[i] > vec[j]:
                vec[i], vec[j] = vec[j], vec[i]

def binary_search(v, x):
    izq, der = 0, len(v) - 1

    while izq <= der:
        c = (izq + der) // 2
        if v[c] == x:
            return c
        if v[c] < x:
            izq = c + 1
        else:
            der = c - 1
    return -1

if __name__ == '__main__':
    vec = array(10)
    print(vec)