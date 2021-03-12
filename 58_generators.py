# generators are used to generate a sequence of object where each item is accessed step by step
def object_created(n):
    for i in range(1, n):
        yield i # yield is used to generate a sequence of values within a range or collection


# instance = object_created
obj1 = object_created(4)


# print(next(obj1))
# print(next(obj1))
# obj2 = instance(4)
# print(next(obj2))


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        global obj1
        o = next(obj1) # next(obj1) is used to access a particular value from sequence once it is called
        return f'Object {o} created'


class B:
    def __init__(self, x, y):
        self.x = y
        self.y = y

    def __repr__(self):
        global obj1
        o = next(obj1)
        return f'Object {o} created'


class C:
    def __init__(self, x, y):
        self.x = y
        self.y = y

    def __repr__(self):
        global obj1
        o = next(obj1)
        return f'Object {o} created'


try:
    o1 = A(2, 3)
    print(o1)
    o2 = B(4, 5)
    print(o2)
    o3 = C(6, 7)
    print(o3)
    o4 = A(8, 9)
    print(o4)
except StopIteration as er:
    print('Too many objects are created')
