_med = ['Paracetamol', 'Bevon', 'Liv52']

print('\nAdd a new element into a list')
_med.append('Crocin')
print(_med)

print('\nList copy')
print('While assigning a list to another variable both refer to the same memory location.\nChange in one list will affect other list also')
_medkart = _med
_medkart[0] = 'Ivermectin'
print(_medkart)
print(_med)

print('\nList copy without changing contents in original list')
print('It will simply copy the contents of a list to a given variable. Change in either variables are not inter dependent')
_medkart = _med[:]
_medkart[0] = 'Cetrizin'
print(_medkart)
print(_med)

print('\nAdd a collection into a list')
_addmed = {'Cetrizin', 'Liv52', 'Pan 40', }  # A set of elements
_med.extend(_addmed)
print(_med)

print('\nPop a given item based on a given index.\nPop the 2nd element from right.')
_med.pop(-2)
print(_med)  # It removed 2nd element from the back(right)

print('\nRemove a given element based on it\'s value')
_med.remove('Crocin')

print(_med)
print('\nInsert a given element in list at a given index')
_med.insert(2, 'Livocet')
print(_med)

print('\nReverse all elements in a list based on index position')
_med.reverse()
print(_med)

print('\nAlternative approach to reverse a list without changing the index positions inside the list')
print(_med[::-1])
print(list(reversed(_med)))
# Difference between sorted function and sort function.
print('\nSort function sorts all elements inside a list and changes are reflected for the same list')
print('\nSorted function returns all elements from a list in sorted order.')
print('\nSorted function doesn\'t make changes to the existing list')
# To sort all elements of a list
print(sorted(_med))

_med.sort(reverse=True)
print(_med)

print('\nIndex of a given element in a list')
_item = 'Liv52'
print('Index of item \'{}\' in list is {}'.format(_item,_med.index(_item)))

print('\nTo count total number of occurrences of a given element in list')
print(_med.count('Liv52'))

print('\nJoin function is used to concatenate items in a list using a given string')
_str = ' || '
print(_str.join(_med))

print('\nRemove all elements in a list')
_med.clear()
print(_med)
