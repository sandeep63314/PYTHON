class flight:
    def __init__(self, _name, _seatname):
        self.name = _name
        self.seatname = {}
        for seat in _seatname:
            self.seatname.update({seat: False})


A = flight('Air Asia', ['W1001', 'M1002', 'L1003', 'W1004', 'M1005', 'L1006', 'W1007', 'M1008', 'L1009'])

B = flight('Vistara', ['W1011', 'M1012', 'L1013', 'W1014', 'M1015', 'L1016', 'W1017', 'M1018', 'L1019'])
