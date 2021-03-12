import pdb
# pdb module is used for debugging. Just like a debugger we can use to check status of execution of each statement.
from functools import reduce


class vehicle:
    def __init__(self, _usr, _name, _dlno):
        self._usr = _usr
        self._name = _name
        self._dlno = _dlno


class finesystem(vehicle):
    fine = {'helmet': 500, 'licence': 1000, 'speed': 500, 'drunk': 200}
    vname = {'T3594': 'Sanjay', 'BQ0076': 'Sandeep', 'S9915': 'Ranjan', 'V7755': 'Rakesh', 'LQ9182': 'Bighna',
             'WR8374': 'Vijaya'}
    lic = {12345, 45678, 67890, 23456, 56789, 89012}

    def __init__(self, _usr, _name, _dlno):
        super().__init__(_usr, _name, _dlno)

    def checklicence(self, _licence):
        pdb.set_trace()
        #set_trace() function is used to check the status of execution of each statement. We can track the assignment of value to each variable.
        # this type of debugging is done to debug any part of your code to check execution of each statement.
        status = True
        try:
            _licno = str(_licence)
            if not (len(_licno[0:]) == 5):
                raise ValueError(False)
        except ValueError as er:
            status = er
        else:
            try:
                if _licence not in self.lic:
                    raise ValueError(False)
            except ValueError as er:
                status = er
            else:
                status = True
        finally:
            return status

    def getamount(self, _finetype):
        return self.fine[_finetype]


fineusers = []
ch = 'y'

A = finesystem('Sanjay', 'TQ2345', 123456)

if (licstatus := A.checklicence(A._dlno)) == True:
    print(licstatus)
    print('DL check passed')
else:
    fineamount = A.getamount('licence')
    fineusers.append({A._name: fineamount})
    print('DL check failed')

while (ch.lower() == 'y'):
    _finetype = input('Enter the type of fine:')
    fineamount = A.getamount(_finetype)
    fineusers.append({A._name: fineamount})
    ch = input('Are there any more fines for vehicle:{} (Y | N) ? '.format(A._name))

print(fineusers)
totalfine = reduce(lambda acc, fineuser: acc + fineuser[A._name], fineusers, 0)
print('Total fine for the user:{}, vehicle:{} is Rs {}/-'.format(A._usr, A._name, totalfine))
