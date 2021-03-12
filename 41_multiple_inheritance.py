class son:
    bank_cash = 500

    def __init__(self, cash, coins):
        self.son_cash = cash
        self.son_coins = coins

    def total_cash(self):
        print(f'Total cash with son:Rs {self.cash}/-, Total coins with son:Rs {self.coins}/-')


class daughter:
    bank_cash = 500

    def __init__(self, cash, coins):
        self.dau_cash = cash
        self.dau_coins = coins

    def total_cash(self):
        print(f'Total cash with daughter:Rs {self.cash}/-, Total coins with daughter:Rs {self.coins}/-')


# Avoid name collision while performing inheritance. Attributes from parent class cannot have the same name as attributes from child class
# Similarly, parameters for parent class attributes inside __init__ function in child class cannot have same name as parameters meant for child class attributes
class father(son,daughter):
    def __init__(self, son_cash, son_coins, dau_cash, dau_coins, cash, coins):
        son.__init__(self, son_cash, son_coins)
        daughter.__init__(self,dau_cash,dau_coins)
        self.dad_cash = cash
        self.dad_coins = coins

    def total_cash(self):
        self.dad_cash = self.dad_cash + self.son_cash + self.dau_cash + son.bank_cash
        self.dad_coins = self.dad_coins + self.son_coins + self.dau_coins


balance = father(100, 10, 500, 50, 1000, 100)
balance.total_cash()
print(f'Total cash of family:Rs {balance.dad_cash}/- and total coins of this family is Rs {balance.dad_coins}/-')
