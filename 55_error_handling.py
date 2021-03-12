age = input('Enter your age:')

def checkage(age):
    try:
        check = int(age)
    except:
        print('This age is invalid. Enter a number')
    else:
        print('This age is valid')

    # check = int(age)
    # print(f'Your age is {check}')

checkage(age)