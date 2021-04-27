#== operator checks equality of 2 values and their type
# is operator checks if 2 values are from same location
print('-----==-----')
print(True == 1) #True evaluates to 1
print(10 == 10.0) # 10 is automatically converted to floating type
print('1' == 1) # string value cannot be equal
print([] == []) # 2 collections are same

a = {10,20}
b = a # a & b are pointing to same memory location
b.add(30)
print(a == b)
print('-----is-----')
print(True is 1) # different memory location
print(10 is 10.0)
print('1' is 1)
print([] is []) # same datastructures but stored in different memory locations

a = {10,20}
b = a # a & b are pointing to same memory location
b.add(30)
print(a is b)

'''
the numbers - 5 to 256 are interned in CPython.Each number is stored at a
singular and fixed place in memory, which saves memory for commonly - used integer.
'''
'''
is operator returns TRUE for below operands if we execute by script
But is operator will return FALSE for below operands if we execute it in console
'''
print('-----Working with intern objects-----')
a = 'hello world'
b = 'hello world'
print(a is b) # value 5 is stored in a fixed memory location

# Use id() to compare identity values of any 2 objects
a = 'hello world'
b = 'hello world'
print(id(a))
print(id(b))