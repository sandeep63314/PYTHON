def encrypt(ch):
    n = ord(ch)
    acc = 0
    while n > 0:
        acc += n
        n -= 1
    return chr(acc)
