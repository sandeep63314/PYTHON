# If we need to use a variable declared outside the function
# then we need to declare it with keyword 'global'
level = 10

def next_level():
    global level
    level += 2

next_level()
print('Welcome to level :',level)