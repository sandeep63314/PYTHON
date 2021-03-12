# read() with mode = 'r' is used to read only the contents of a file based on starting position(_file.seek(0)). Default starting position is 0.
# write() with mode = 'w' is used to create/recreate a file and write contents into it from beginning.
# write() with mode = 'r+' stands for read and write. It is used to overwrite characters at the beginning of the file with rest characters appended to it.
# write() with mode = 'a' is used to append characters at the end of a file.
with open('mergeTextFile.txt', mode = 'w') as _writefile:
    _writefile.write('Joe Biden became the 46th president of USA.')

# _file = open('mergeTextFile.txt')
# print(_file.read())

with open('mergeTextFile.txt', mode = 'a') as _appendmyfile:
    _appendmyfile.write('\nDr. Jill Biden is made the 1st lady of USA.')
    _appendmyfile.write('\nKamala Harris became the vice president of USA')

# _file = open('mergeTextFile.txt')
# print(_file.read())
#
# with open('mergeTextFile.txt', mode = 'r+') as _readwritefile:
#     _readwritefile.write('On 21st Jan 2021 ')

_content = open('aboutBiden.txt')
_Biden = _content.read()

_content = open('aboutKamala.txt')
_Kamala = _content.read()

with open('mergeTextFile.txt', mode = 'a') as _appendmyfile:
    _appendmyfile.write('\n-----------------\nAbout Joe Biden\n-----------------\n')
    _appendmyfile.write(_Biden)
    _appendmyfile.write('\n-----------------\nAbout Kamala Harris\n-----------------\n')
    _appendmyfile.write(_Kamala)