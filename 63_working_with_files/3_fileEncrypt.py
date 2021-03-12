from functools import reduce
import encrypt

_f = open('mergeTextFile.txt')
_content = _f.read()
_content = list(_content)

_encContent = reduce(lambda acc,c : acc + encrypt.encrypt(c),_content,'')

with open('encryptFile.txt',encoding='utf-8',mode = 'w') as _encfile:
    _encfile.write(_encContent)