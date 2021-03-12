# Decorator is a methodology where a function accepts another function as a argument and returns a function.
# The function passed as a parameter is called inside a wrapper function.
# Behavior of a function with a decorator
def calculator(func):
    operator = input('Choose your operator \'+\',\'-\',\'*\',\'/\':')

    # In the wrapper function we pass the parameters used as arguments inside the function.
    def wrapper_func(x, y):
        nonlocal operator
        sign = operator
        x = float(x) + 10
        y = float(y) + 10
        if (sign == '+'):
            a, b = func(x, y)
            a = float(a)
            b = float(b)
            total = a + b
        elif (sign == '-'):
            a, b = func(x, y)
            a = float(a)
            b = float(b)
            total = a - b
        elif (sign == '*'):
            a, b = func(x, y)
            a = float(a)
            b = float(b)
            total = a * b
        elif (sign == '/'):
            a, b = func(x, y)
            a = float(a)
            b = float(b)
            total = a / b
        else:
            total = 'Invalid operator'
        return total

    return wrapper_func


# @calculator allows getnumbers() function to be called inside a wrapper function of a higher order function.
# It allows to make modifications with arguments passed within the called function inside the higher order function.
@calculator
def getnumbers(n, m):
    return n, m


num1 = input('Enter the first number:')
num2 = input('Enter the second number:')

print(getnumbers(num1, num2))


# Behavior of a function without a decorator
def getnumbers(n, m):
    return n, m


num1 = input('Enter the first number:')
num2 = input('Enter the second number:')

print(getnumbers(num1, num2))
