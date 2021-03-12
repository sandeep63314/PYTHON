# value of hike is overwritten inside the function
salary = 101010.00
hike = 10


def salary_hike(sal):
    hike = 5
    return sal + ((hike / 100) * sal)


print(salary_hike(salary))

# since no local variable hike is present inside the function therefore parent variable is taken into picture
salary = 101010.00
hike = 10


def salary_hike(sal):
    #hike += 1 # UnboundLocalError: local variable 'hike' referenced before assignment
    return sal + ((hike / 100) * sal)


print(salary_hike(salary))
