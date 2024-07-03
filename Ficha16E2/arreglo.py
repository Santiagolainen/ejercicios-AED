import random

def array(n):
    vec = []
    for i in range(n):
        num = random.randint(4000, 5000)
        vec.append(num)
    return vec

def ord_men_may(v):    
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

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
