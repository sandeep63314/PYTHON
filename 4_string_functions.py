_addr = 'S/2-532,Niladrivihar,Bhubaneswar'
# concatenation of string
_addr = _addr + ',Odisha'
print(_addr)
# Length of a string
_l = len(_addr)
# Use of escape sequence '\' in prompt
print('Length of string \'_addr\' is ' + str(_l))
# slicing a given string. Getting substring of a string.
# Starting position can be +ve or -ve. Ending position can be +ve or -ve
_substr = _addr[0:7]
print(_substr)
_substr = _addr[-18:-7]
print(_substr)
# Reverse a given string. 3rd argument used to mention the intervals to pick characters
_substr = _addr[::-1]
print(_substr)
# Replace any given substring in a string.
# Here replace only 1 ',' with '\n'
_replacestring = _addr.replace(',', '\n', 1)
print(_replacestring)
# Split a string based on a given substring into a list collection.
# Here split a string 2 times for ',' character
_lines = _addr.split(',', 2)
print(_lines)
# Remove substring from start or end of string. I have stripped 'N' from beginning of string
# Here mention any character that needs to be stripped off from beginning and end
_stripping = _lines[1].strip('N')
print(_stripping)
# Index of a given substring in string
# Find the next index of ',' starting at index number 8 till the end
_indx = _addr.index(',', 8)
print(_indx)
# To create a long string written in any desired format. To retain the format
longstr = '''
S/2-532
Niladrivihar
Bhubaneswar
Odisha'''
print(longstr)
