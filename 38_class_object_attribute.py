class account:
    # class object attribute. This attribute can be directly accessed outside the class using class name
    active = True

    def __init__(self, _accountname, _userid, _balance):
        # Unlike class object attributes, class attributes are dynamic
        if self.active == True:  # You can also mention it as account.active == True
            self.accountname = _accountname
            self.userid = _userid
            self.balance = _balance
        else:
            self.accountname = None
            self.userid = None
            self.balance = None

    def min_balance(self):
        return (False if self.balance < 2000 else True)


_acct1 = account('121', 'Jesse', 4000)
_acct2 = account('555', 'Walter', 1000)
_users = []
_users.append(_acct1)
_users.append(_acct2)
_addmoney = 'Y'

while _addmoney.lower() == 'y':
    if _users.__len__() > 0:
        for u in _users:
            status = u.min_balance()
            if status:
                print(f'Thank you!!! \'{u.userid}\' can withdraw.')
                _users.remove(u)
            else:
                print(f'\'{u.userid}\' has insufficient balance to withdraw')
                addmoney = input("Do you wish to add money. Press 'Y' for Yes and 'N' for No:")
                if _addmoney.lower() != 'y':
                    break
                addcash = input('Enter cash:')
                u.balance += int(addcash)
    else:
        _addmoney = 'N'
