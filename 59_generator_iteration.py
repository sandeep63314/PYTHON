orders = [11000,12100,12300,23400]
# We can generate each value from a collection without yielding.
# iter function generates the memory location where collection of objects are stored
a = iter(orders)
print(a)
try:
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
except StopIteration as er:
    print('Out of range')