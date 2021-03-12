_my_set = {'pen', 'pen', 'pencil', 'eraser', 'book', 'eraser'}
_set_1 = _my_set.copy()  # copies the entire set into another set
print(_set_1)

# add() to add an item to a set
_my_set.add('crayon')
_my_set.add('scale')
_my_set.add('rounder')
print(_my_set)

print('\ndifference() is used to find those elements from a set that is not present in another set')
# difference() doesn't make any changes to the original set
_set_1 = {'pen', 'pencil', 'eraser'}
print(_my_set.difference(_set_1))

print('\ndifference_update() is used to remove elements from one set present in another set')
_set_1 = _my_set.copy()
_set_2 = {'pen', 'pencil', 'eraser'}
_set_1.difference_update(_set_2)
print(_set_1)

print('\ndiscard() is used to remove an element from a set')
_my_set.discard('pen')
print(_my_set)

print('\nintersection() is used to print common items between 2 sets')
_set_1 = _my_set.copy()
_set_2 = {'pen', 'pencil', 'eraser'}
print(_set_1.intersection(_set_2))
print(_set_1 & _set_2)

print('\nunion() is used to print all items from 2 sets')
_set_1 = _my_set.copy()
_set_2 = {'stapler', 'puncher', 'files'}
print(_set_1.union(_set_2))
print(_set_1 | _set_2)

print('\nis disjoint() is used to check if 2 sets are unique and have no common items')
_set_1 = {'pen', 'pencil', 'eraser'}
_set_2 = {'stapler', 'puncher', 'files'}
print(_set_1.isdisjoint(_set_2))

_set_1 = {'pen', 'pencil', 'eraser', 'stapler'}
_set_2 = {'stapler', 'puncher', 'files'}
print(_set_1.isdisjoint(_set_2))

print('\nissubset() is used to check if all elements in a set is present in another set')
_set_1 = {'pen', 'pencil'}
_set_2 = {'pen', 'pencil', 'eraser', 'stapler'}
print(_set_1.issubset((_set_2)))

_set_1 = {'pen', 'pencil', 'eraser', 'stapler'}
_set_2 = {'pen', 'pencil'}
print(_set_1.issubset((_set_2)))

print('\nissuperset is used to check if a set contains all elements present in another set')
_set_1 = {'pen', 'pencil', 'eraser', 'stapler'}
_set_2 = {'pen', 'pencil'}
print(_set_1.issuperset(_set_2))

_set_1 = {'pen', 'pencil'}
_set_2 = {'pen', 'pencil', 'eraser', 'stapler'}
print(_set_1.issuperset(_set_2))