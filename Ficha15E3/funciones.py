def nums_prim(num, nprimos):
    ntp = False
    if num == 2 or num == 3:
        nprimos.append(num)
    else:
        for i in range(2, num**1//2 + 1):
            if num % i == 0:
                ntp = True
                break
        if not ntp:
            nprimos.append(num)


def prom(n1, n2):
    if n2 != 0:
        return n1 // n2
    return 0
                    