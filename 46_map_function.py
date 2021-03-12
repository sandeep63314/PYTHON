# Functional programming defines pure functions that work on data(iterables) to produce same output that doesn't change after multiple executions
# Map function is used to work with each element of iterables passed as argument in it and returns a iterable list,tuple or set.

# Though 'inc' is not iterable but I have passed it as a default parameter

def salary_increment(salary, inc=10):
    return ((100 + inc) / 100) * salary


_sal = [25000, 30000, 40000]
_salaries = tuple(map(salary_increment, _sal))

print(_salaries)