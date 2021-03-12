# class is used to create user defined object of customisable type.
# Two distinct classes cannot be of same type unless they are equal to each other.
class _airline:
    # __init__ function is used to assign values to attributes
    def __init__(self, _flight, _airport):
        # self is a default parameter in every function
        # self is used to call the class attributes
        # self refers to the class to access class attributes
        self._flight = _flight
        # self.airport is overwritten
        self._airport = 'Dubai International Airport'

    def _flightCategory(self):
        print(self._flight)
        print(self._airport)


# Class instantiation called as object.
_vehicle = _airline(
    [['B747', '20-12-2020 14:00:00', '20-12-2020 15:00:00'], ['D555', '20-12-2020 15:30:00', '20-12-2020 16:30:00'],
     ['A1100', '20-12-2020 17:30:00', '20-12-2020 18:30:00']], 'London Airport')

# class object is used to access class attributes using .(dot) operator
for _vehicletype in _vehicle._flight:
    if _vehicletype[0][0] == 'B':
        print(f'{_vehicletype[0]} is a boeing.')
    elif _vehicletype[0][0] == 'A':
        print(f'{_vehicletype[0]} will fly to abroad.')
    elif _vehicletype[0][0] == 'D':
        print(f'{_vehicletype[0]} will fly to domestic international airport.')
    else:
        print('UFO. More details are required')
_vehicle._flightCategory()
