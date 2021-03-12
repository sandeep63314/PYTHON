# list comprehension is used to create list of values from a given list
# list comprehension is an alternative method of using map and filter on a list
# Both map and filter action can be used in list comprehension

rng = range(100)

# Creates a list of items, for each item in range object
list1 = [item for item in rng]
print(list1)

# Creates a list of item * 2, for each item in range object
list2 = [item * 2 for item in rng]
print(list2)

# Creates a list of items, for each item in range object where item % 2 == 0
list3 = [item for item in rng if item % 2 == 0 and item % 3 == 0]
print(list3)