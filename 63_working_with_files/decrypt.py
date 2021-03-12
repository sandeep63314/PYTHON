import math


def decrypt(ch):
    n = ord(ch)
    c = (-1) * n * 2
    a = 1
    b = 1
    roots = []
    D = math.pow(b, 2) - (4 * a * c)
    if D > 1:
        r = ((-1) * b - math.sqrt(D)) / (2 * a)
        roots.append(r)
        r = ((-1) * b + math.sqrt(D)) / (2 * a)
        roots.append(r)
        for val in roots:
            if val > 0:
                r = int(val)
    elif D == 0:
        r = ((-1) * b) / (2 * a)
    else:
        try:
            raise ValueError(-1)
        except ValueError as er:
            r = -1
    return chr(r)
