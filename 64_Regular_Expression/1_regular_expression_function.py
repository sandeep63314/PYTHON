import re

# compile() takes any string pattern as it's input
pattern = re.compile('20-12-2020')

string = 'goSmart 20-12-2020 London Youtube 20-12-2020'

# search() searches for a given string pattern in the main string
search = pattern.search(string)
print(search)
# span() gives the index value(start position , end position) of first match of string pattern
print(search.span())
# returns the first string that matches the given string pattern
print(search.group())

# returns list of all matches with the string pattern
findall = pattern.findall(string)
print(findall)

# fullmatch() matches a given string pattern with a full string starting from beginning by default
pattern = re.compile('goSmart 20-12-2020 London Youtube 20-12-2020')
fullmatch = pattern.fullmatch(string)
print(fullmatch)

# match() matches a given string pattern with part of a string starting from beginning by default
pattern = re.compile('20-12-2020')
match = pattern.match(string)
print(match)