# open function is used to open a file
# readlines() is used to create a list of all sentences in a file
_file = open('crimerecord.csv')

_filecontents = _file.readlines()

print(_filecontents)

for _sentence in _filecontents:
    print(_sentence)

print('---------------------------------------------------------------------------------')
# read() is used to read the contents of a file
_file = open('crimerecord.csv')

_filecontents = _file.read()

print(_filecontents)

print('---------------------------------------------------------------------------------')
# readline() is used to read the contents of a line at a particular index position
_file = open('crimerecord.csv')

#seek() is used to take the cursor to a particular index position in a file
_file.seek(7)

#Once readline() read the current line starting at index 0 in the file it reaches end of the line followed by '\n'
print(_file.readline())
#Next time when readline() is called it reads the next line
print(_file.readline())
print(_file.readline())
print(_file.readline())

# close() is used to close a file
_file.close()