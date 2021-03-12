def seattype(_type, *args):
    totalseats = []
    seatavail = []
    for plane in args:
        # for seat, status in plane.seatname.items():
        #     if seat[0] == _type and status == False:
        #         seatavail.append(seat)
        #         totalseats.append(seat)
        seatavail = [seats for seats, status in plane.seatname.items() if seats[0] == _type and status == False]
        totalseats.extend(seatavail)
        print(plane.name)
        print(seatavail)
        seatavail = []
    return totalseats


def seatbooking(_type, _name, _seatnumber, _confirm, *args):
    for flight in args:
        if flight.name == _name:
            f = [flt for flt in flight.seatname.keys() if flight.seatname[flt] == False and flt[0] == _type]
            # fnot = [flt for flt in flight.seatname.keys() if flight.seatname[flt] == False]
            if _seatnumber in f and _confirm.lower() == 'y':
                flight.seatname[_seatnumber] = True
                return _seatnumber
            # elif _seatnumber in fnot and _confirm.lower() == 'y':
            #     return -2
            # else:
            #     return -1


def checkemptyseats(_type, _name, *args):
    for flight in args:
        if flight.name == _name:
            emptyseats = [flt for flt in flight.seatname.keys() if flight.seatname[flt] == False and flt[0] == _type]
            return emptyseats