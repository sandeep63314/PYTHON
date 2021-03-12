#To read a string silently as input
import getpass
import hashlib

_pwd = getpass.win_getpass(prompt = 'Password:', stream = None)

_result = hashlib.md5(_pwd.encode())
if (_result.hexdigest() == '179ffaa9f8677595956d98a29905c077'):
    print('Authentication successful')
else:
    print('Incorrect password. Please try again...')