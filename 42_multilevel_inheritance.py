class bank:
    def __init__(self, _name, _branch, _balance):
        self.name = _name
        self.branch = _branch
        self.balance = _balance
        print('calling bank')


class rbi(bank):
    def __init__(self, _balance, _name, _branch, _amount):
        super().__init__(_name, _branch, _amount)
        self.balance = _balance
        print('Calling rbi')


class worldbank(rbi):
    def __init__(self, _balance, _total, _name, _branch, _amount):
        super().__init__(_total, _name, _branch, _amount)
        self.balance = _balance
        print('Calling worldbank')


_wrld_bal = 2500000
_rbi_bal = 1000000
_bank_nm = 'UBI'
_branch = 'Chandrasekharpur'
_bank_bal = 500000
_wrld = worldbank(_wrld_bal, _rbi_bal, _bank_nm, _branch, _bank_bal)

_rbi_bal += _bank_bal
_wrld_bal += _rbi_bal
_bank_nm = 'PNB'
_branch = 'Chandrasekharpur'
_bank_bal = 750000

_wrld = worldbank(_wrld_bal, _rbi_bal, _bank_nm, _branch, _bank_bal)

_rbi_bal += _bank_bal
_wrld_bal += _rbi_bal

print('Total amount present in {} is Rs {}/-'.format('RBI', _rbi_bal))
print('Total amount present in {} is Rs {}/-'.format('Worldbank', _wrld_bal))

print(_wrld.__dir__())