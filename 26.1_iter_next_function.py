try:
    x = list(range(1,6))
    y = iter(x)
    while True:
        z = next(y)
        print(z)
except StopIteration:
    print('List is completed')