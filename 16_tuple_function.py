# There are only 2 functions in tuple
# count & index
delivery_pin = (751021, 751024, 751001, 751021, 751027)

print(delivery_pin.count(751021))

# index function returns the index position of first occurrence of a item
print(delivery_pin.index(751024))

# Tuple slicing. You can retrieve a part of a tuple
print(delivery_pin[2:3])
print(len(delivery_pin[2:3]))