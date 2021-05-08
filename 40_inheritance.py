class ubi:
    _name = 'UBI'
    _total = 500000
    _limit = (50 / 100) * _total

    def __init__(self, _loan):
        self.loan = _loan

    def loan_eligibility(self):
        if ((ubi._total - self.loan) < ubi._limit):
            return False
        else:
            ubi._total -= self.loan
            return ubi._total


# _credit = input('Enter your loan amount:')
# _cash = ubi(int(_credit))
# _amount = _cash.loan_eligibility()
# print(f'Total cash with UBI is Rs {_amount}/-' if _amount else 'UBI cannot offer you loan')
# #ubi._limit = (50/100) * ubi._total
# print(ubi._total,ubi._limit)
#
# _credit = input('Enter your loan amount:')
# _cash = ubi(int(_credit))
# _amount = _cash.loan_eligibility()
# print(f'Total cash with UBI is Rs {_amount}/-' if _amount else 'UBI cannot offer you loan')
# #ubi._limit = (50/100) * ubi._total
# print(ubi._total,ubi._limit)

class boe:
    pass


# I have passed parent class 'ubi' as parameter inside child class 'rbi'
# According to inheritance property 'rbi' will now be able to use attributes,functions of 'ubi'
class rbi(ubi):
    _reserve = 1500000
    _limit = (50 / 100) * _reserve

    def __init__(self, _bankloan, _loan):
        ubi.__init__(self,_loan)
        self._bankloan = _bankloan

    def total_cash(self):
        # As discussed above parent class attributes can be called now inside child class
        ubi._total += self._bankloan
        return ubi._total

    def loan_eligibility(self):
        if ((rbi._reserve - self._bankloan) < rbi._limit):
            return False
        else:
            rbi._reserve -= self._bankloan
            return rbi._reserve


_credit = eval(input('Enter loan amount to be taken by UBI:'))
_userloan = eval(input('Enter loan amount to be taken by UBI customer:'))
_cash = rbi(_credit,_userloan)
# Polymorphism : If there is a name collision between parent class attributes, functions and child class attributes, functions then you can create corresponding object instances to call respective attributes, functions.
_amount = _cash.loan_eligibility()
# Attributes of parent class can be accessed and called inside child class because child class is inheriting properties of parent class.
print(f'Total cash with RBI is Rs {_amount}/-' if _amount else f'RBI cannot offer this bank {ubi._name} any loan')
_bankcash = _cash.total_cash()
print(f'Total cash with UBI now is Rs {_bankcash}/-')
_ubibal = ubi(_cash.loan)
_bankcash = _ubibal.loan_eligibility()
print(f'Total cash with UBI after loan disbursement is Rs {_bankcash}/-')

# You can pass a tuple containing name of all class to check if a object instance belong to any of those classes
print(isinstance(_cash, (ubi, rbi)))
# this will return false because 'rbi' is not inheriting any properties from 'boe'.
# So, '_cash' object instance cannot call any attributes, functions that belong to 'boe' class
print(isinstance(_cash, boe))
