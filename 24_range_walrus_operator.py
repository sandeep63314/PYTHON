# range(start, end, step over) is used to create a list of numbers from start and less than end value
_iq = input('Enter your _iq:')
# _iq = int(_iq)
# If variable declaration is not needed in for loop then we can use '_'.
# Used walrus operator to assign int(_iq) to _
if (_ := int(_iq)) in range(100, 121, 1):
    # list function is used to convert range into a list
    print('You are good')
elif _ in range(121, 151, 1):
    print('You have an average _iq')
elif _ in range(151, 181, 1):
    print('You are brilliant')
elif _ in range(181, 201, 1):
    print('You are a genius')
elif _ > 200:
    print('You are Einstein')
else:
    print('You need to improve your _iq')
