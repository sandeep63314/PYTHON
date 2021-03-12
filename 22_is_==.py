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
print('-----is------')
print(True is 1) # different memory location
print(10 is 10.0)
print('1' is 1)
print([] is []) # same datastructures but stored in different memory locations

a = {10,20}
b = a # a & b are pointing to same memory location
b.add(30)
print(a is b)