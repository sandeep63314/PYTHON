from functools import reduce


# Higher order function is a function that either accepts function as a parameter or returns a function.
# map,filter & reduce are all higher order functions. They accept function as argument.
def str_len(fullname, fname, lname):
    name = fullname(fname, lname)
    print(f'Length of your name:\'{name}\' is {name.__len__()}')


def fullname(first, last):
    return first + ' ' + last


fn = input('Enter your first name:')
ln = input('Enter your last name:')

string = str_len

print(string(fullname, fn, ln))