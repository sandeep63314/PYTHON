class employee:
    def __init__(self, _empid, _name, _dept):
        self.empid = _empid
        self.name = _name
        self.dept = _dept

    def __call__(self, *args, **kwargs):
        print('Employee object instance is created')

    def __mul__(self, other):
        return 'You are multiplying 2 numbers'

    def __repr__(self):
        return 'Printing a string instead of memory address'

    def __delattr__(self, item):
        return 'Deleting a class attribute:' + item


emp = employee(705306, 'Sangram', 'ENU')
print(emp)  # __repr__
emp.__setattr__('empid', 1620775)
print(emp.empid)  # __setattr__ is used to set a value to a class attribute
print(emp.__getattribute__('name'))  # __getattribute__ is used to get the value from a class attribute
num1, num2 = 3, 4
print(emp * num2)
print(emp.__getattribute__('dept'))

delattr = emp.__delattr__('dept')
print(delattr)

print(emp.__getattribute__('dept'))
