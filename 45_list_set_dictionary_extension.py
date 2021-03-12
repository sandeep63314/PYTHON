class _foodorder(dict):
    def __init__(self, _user, _addr, _datetime):
        self.user = _user
        self.addr = _addr
        self.datetime = _datetime


_order = _foodorder('Monty', '111 Brooklyn Street, New York', '25-12-2020 10:15:30')
fooditem = {'Pizza', 'Croissant', 'Patties', 'Sandwich', 'Cuttlet'}
choice = 'y'
while choice.lower() == 'y':
    item = input('Enter your food:')
    if item in fooditem:
        quantity = input(f'Enter number of {item}\'s:')
        _order.update({item:int(quantity)})
    else:
        print('Sorry :( The food is not available in our list.')
    choice = input('Do you still want to continue. Press \'y\' to continue or press \'n\' to abort.')

print('Your order details are as below: -')
for i,j in _order.items():
    print(i,j)