import sys
import re
# Exception handling is used to manually handle any type of error.
# try block : In this block you place only those part of code that is assumed to generate an error
# except : If a try block generates any error it is handled in except block. Exception can be customised to handle any specific type of exception.
#          If a try block generates any error a specific course of action can be placed in except block after error has occured.
# else : If a try block doesn't generates any error then you can mention a specific course of action in else block to perform.
# finally : In this block the rest part of your code needs to placed that you want to execute after exception handling.
try:
    check = input('Enter your age:')
    age = re.search('\D',check)
    if age.span() != None:
        raise TypeError('Enter a integer value')
    if int(check) < 0:
        raise ValueError(f'This age is invalid. Enter a number greater than 0')
except (ValueError, ZeroDivisionError) as er:
    print(sys.exc_info())
    print(er)
except TypeError as er:
    print(er)
else:
    print('This age is valid')
finally:
    if check > 18:
        print('You are eligible to ride a 2 wheeler')
    else:
        print('You are not eligible to ride a 2 wheeler')
