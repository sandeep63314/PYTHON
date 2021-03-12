# Modules are the python scripts  present at different location
# A package can contain several modules
# If we want to use a module present in a different package then we need to import it
# Once a module is imported we can access objects in it using module itself
# We can import selected modules from a package using 'from' keyword

from flightbooking.flightbooking import A, B
from flightbooking.functions import seattype, seatbooking, checkemptyseats
import random

# if __name__ == '__main__':
#     ch = 'y'
#     while ch.lower() == 'y':
#         _seattype = input('Enter your seat type (W | M | L):')
#         _seatpresent = A.seattype(_seattype)
#         print(_seatpresent)
#         try:
#             if _seatpresent == []:
#                 raise IndexError(
#                     f'Sorry, no further seats are available for the current seat type. Choose another seat type')
#         except IndexError as er:
#             print(er)
#         else:
#             _seatnum = input('Choose your desired seat number:')
#             try:
#                 if _seatnum not in _seatpresent:
#                     raise IndexError('Your desired seat in not available. Please try again...')
#             except IndexError as er:
#                 print(er)
#             else:
#                 _status = input('Kindly, confirm to proceed (Y | N):')
#                 try:
#                     if _status.lower() not in ('y', 'n'):
#                         raise ValueError('Please provide your correct input (Y | N)')
#                 except ValueError as er:
#                     print(er)
#                 else:
#                     _seatstatus = A.seatbooking(_seatnum, _seatpresent, _status)
#                     print('Your flight ticket has been booked with seatnumber:{} in {}'.format(_seatstatus, A.name))
#                     ch = input('Do you want to continue (Y | N):')

# __name__ is used to get name of the current module
# if any module imports other packages,modules then name of the main module is __main__
if __name__ == '__main__':
    _flts = [A, B]

    ch = 'y'
    while ch.lower() == 'y':
        _seattype = input('Enter your seat type (W | M | L):')
        try:
            if _seattype not in ('W', 'M', 'L'):
                raise ValueError('Please choose a correct seat type again...')
        except ValueError as er:
            print(er)
        else:
            _seatpresent = seattype(_seattype, A, B)
            try:
                if _seatpresent == []:
                    raise IndexError(
                        f'Sorry, no further seats are available for the current seat type. Please choose another seat type...')
            except IndexError as er:
                print(er)
            else:
                _name = input('Enter the name of your flight:')
                try:
                    if _name not in (A.name, B.name):
                        raise ValueError('Please choose the correct flight again...')
                except ValueError as er:
                    print(er)
                else:
                    _totalseats = checkemptyseats(_seattype, _name, A, B)
                    try:
                        if _totalseats == []:
                            raise IndexError(
                                f'No seats are available for the selected seat type in flight:{_name}. Please choose another seat type or any another flight for same seat type...')
                    except IndexError as er:
                        print(er)
                    else:
                        _seatnum = random.choice(_totalseats)
                        _status = input('Kindly, confirm to proceed (Y | N):')
                        try:
                            if _status.lower() == ('n'):
                                raise ValueError(
                                    'You haven\'t chosen to proceed. Please book your ticket once again if you like our service...')
                            elif _status.lower() not in ('y', 'n'):
                                raise ValueError('Please provide your correct input (Y | N)...')
                        except ValueError as er:
                            print(er)
                        else:
                            _seatstatus = seatbooking(_seattype, _name, _seatnum, _status, A, B)
                            # try:
                            #     if _seatstatus == -1:
                            #         raise ValueError(
                            #             f'Your desired seat in not available in flight:{_name}. Please choose the one that is available in flight:{_name}...')
                            #     elif _seatstatus == -2:
                            #         raise ValueError(
                            #             f'Your select seat doesn\'t matches with the type you had selected. Please choose a seat from your selected type in flight:{_name}...')
                            # except ValueError as er:
                            #     print(er)
                            # else:
                            print(
                                'Your flight ticket has been booked with seatnumber:{} in {}'.format(_seatstatus,
                                                                                                    _name))
        finally:
            ch = input('Do you want to continue (Y | N):')
