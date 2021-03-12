age = input('Enter your age:')


def checkage(age):
    try:
        check = int(age)
    except (ValueError, ZeroDivisionError) as er:
        print(f'This age is invalid. Enter a number greater than 0 \n{er}')
    else:
        print('This age is valid')
    finally:
        try:
            if int(age) > 18:
                print('You are eligible to ride a 2 wheeler')
            else:
                # It is possible to manually raise an exception. Once you raise a except that needs to be caught and handled.
                raise Exception('You are not eligible to ride a 2 wheeler')
        except Exception as err:
            print('You are fined Rs 2000/-')

    # check = int(age)
    # print(f'Your age is {check}')


checkage(age)
