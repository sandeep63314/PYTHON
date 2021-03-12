from functools import reduce

# Simple pure functions can be written using lambda expressions. They reduce our lines of code.
# So, instead of function name passed as argument in map function we give lambda expression.
# lambda expressions evaluates only once for each item but passes those values into either map, filter or reduce function.
dimension = [10, 20, 30]

# lambda x : where x is each item from the collection mentioned
print(list(filter(lambda x: x >= 20, dimension)))

dimension = [40, 50, 60]
print(list(map(lambda x: (x/10), dimension)))

dimension = [70, 80, 90]
# lambda acc, x : where acc is the accumulator with default value 0 and x is each item from collection mentioned
print(reduce(lambda acc, x: acc + x, dimension))

# Q. Sort all elements inside the list based on 2nd element inside the tuples
dimension = [(1, 2), (4, 3), (10, -1), (9, 9)]

# key are the set of elements based on which list is going to be sorted.
# key takes list of all 2nd values in tuples inside the list.
dimension.sort(key=lambda x: x[1])

print(dimension)
