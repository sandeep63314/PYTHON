#_my_list = range(10)
_my_mobile = input('Enter your mobile number:')
flag = True

for i in _my_mobile:
    i = ord(i)  # ord function returns the ascii value of a string of length 1
    if not 48 <= i <= 57:
        print('This is not a valid mobile number')
        flag = False
        break
if flag:
    print('This is a valid mobile number')
