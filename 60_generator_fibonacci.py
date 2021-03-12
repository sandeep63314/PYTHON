def fibonacci(n):
    a, b, c = (0, 1, 0)
    print(a)
    print(b)
    for i in range(n):
        c = a + b
        yield c
        a = b
        b = c


fib = fibonacci(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
#-----------------------------------------------------------------------
def fibonacci(n):
    a, b, c = (0, 1, 0)
    for i in range(n):
        c = a
        yield a
        a = b
        b = c + b


fib = fibonacci(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
#-----------------------------------------------------------------------
def total_price(acc,item):
    for tot in iter(item):
        acc += tot
        yield acc
acc,food_price = 0,[100,200,300,400,500]
amount = total_price(acc,food_price)
try:
    print(next(amount))
    print(next(amount))
    print(next(amount))
    print(next(amount))
    print(next(amount))
    print(next(amount))
except StopIteration as er:
    print(er)