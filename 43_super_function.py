class _stationaries:
    def __init__(self, _items, _price):
        self.items = _items
        self.price = _price

    def _total_price(self):
        total = 0
        for name, num in self.items.items():
            if name in self.price.keys():
                total += (self.price[name] * num)
        return total


class _store(_stationaries):
    # If a class is inheriting from a super class then given class has to pass parameters for all attributes of super class.
    def __init__(self, _name, _date, _items, _price):
        # By calling super() function we are initializing attributes of super class with parameters passed in __init__ function of current class.
        # Instead of super() function you can use _stationaries.__init__(self,_items,_price)
        # Super function avoids use of self keyword as it's parameter
        super().__init__(_items, _price)
        self.name = _name
        self.date = _date

    def _store_type(self, total):
        if total < 1000:
            return 'Small scale enterprise'
        elif 1000 <= total < 10000:
            return 'Medium scale enterprise'
        else:
            return 'Large scale enterprise'


_type = _store('Janaki', '24-12-2020', {'Perfume': 10, 'Powder': 8, 'Nailpolish': 15, 'Banglesets': 20},
               {'Perfume': 200, 'Banglesets': 50})
# Object instance of main class can now access attributes,functions of super class because we have passed super() function inside __init__() function of main class.
print(_type.items)
print(_type.price)
_amount = _type._total_price()
print(f'Total price of {_type.name} is Rs {_amount}/-')
check = _type._store_type(_amount)
print(f'{_type.name} is a {check}')