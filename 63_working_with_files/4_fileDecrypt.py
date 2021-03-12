from functools import reduce
import decrypt

_f = open('encryptFile.txt', encoding='utf-8')
_content = _f.read()
_content = list(_content)

_decContent = reduce(lambda acc, c: acc + decrypt.decrypt(c), _content, '')

with open('decryptFile.txt', mode='w') as _decfile:
    _decfile.write(_decContent)
