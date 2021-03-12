# Docstring is used to add more briefing/description to a program
def add(num1,num2):
    '''
    This function is used to add 2 numbers
    '''
    return num1 + num2

a,b = 10,20
print(add(a,b))
print(add.__doc__)
