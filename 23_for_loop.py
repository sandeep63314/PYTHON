from functools import reduce
_employee = {
    '_empid' : 1122334455,
    '_name' : 'Sangram Mohanty',
    '_company' : 'Tesla'
}
for _val in _employee:
    print(_val)

print('\n---Keys---\n')
for _keys in _employee.keys():
    print(_keys)

print('\n---Values---\n')
for _values in _employee.values():
    print(_values)

print('\n---Items(Keys & Values)---\n')
for _items in _employee.items():
    print(_items)

print('\n---Iterating through collection---\n')
_cars = ['Toyota','BMW','Ferrari']
for _val in _cars:
    print(_val)

print('\nSum of price of all grocery items\n')
_grocery = {'rice':45,'dal':60,'noodles':50}
# _total = 0
# for price in _grocery.values():
#     _total += price
_total = reduce(lambda x,acc : acc + x, _grocery.values(),0)
print('Total price of all grocery items:',_total)

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for i in picture:
    for j in i:
        print(' ' if j == 0 else '*', end = ' ') # Used ternary operator
    print('\n', end='')