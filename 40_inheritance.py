# Golden rule of inheritance ::: Avoid attribute name collision across classes used in inheritance. It causes ambiguous behavior in value initialisation
class father:
    def __init__(self,balance,cash,coins):
        self.balance = balance
        self.cash = cash
        self.coins = coins
    def cash_display(self):        
        print(f'Father is left with total bank balance amount of Rs{self.balance}/-.')
        print(f'Father is left with total cash amount of Rs{self.cash}/-.')
        print(f'Father is left with total coin amount of Rs{self.coins}/-.')
        print('--------------------------------')

class son(father):
# class "son" is inheriting all properties(attributes, methods) of class "father"
# It can call all properties of class "father" using object instances/class objects outside the class definition and access parent class("father") properties using self keyword inside child class definition("son")
    ratio = 0.6
    def __init__(self,balance,cash,coins):
        # child class need to pass all parameters of parent class in it's __init__ method
        # After that it needs to call parent class __init__ methods with it's arguments(arguments are taken from child class parameters defined in it's __init__ class)
        father.__init__(self,balance,cash,coins)
        
        self.sbalance = son.ratio * self.balance
        self.scash = son.ratio * self.cash
        self.scoins = son.ratio * self.coins
    def cash_display(self):
        print(f'Son has total bank balance amount of Rs{self.sbalance}/-.')
        print(f'Son has total cash amount of Rs{self.scash}/-.')
        print(f'Son has total coin amount of Rs{self.scoins}/-.')
        print('--------------------------------')
        self.balance = (1 - son.ratio) * self.balance
        self.cash = (1 - son.ratio) * self.cash
        self.coins = (1 - son.ratio) * self.coins
        print(f'Father is left with total bank balance amount of Rs{self.balance}/-.')
        print(f'Father is left with total cash amount of Rs{self.cash}/-.')
        print(f'Father is left with total coin amount of Rs{self.coins}/-.')
        print('--------------------------------')

class mother:
    def __init__(self,balance,cash,coins):
        self.mbalance = balance
        self.mcash = cash
        self.mcoins = coins
    def cash_display(self):        
        print(f'Mother is left with total bank balance amount of Rs{self.balance}/-.')
        print(f'Mother is left with total cash amount of Rs{self.cash}/-.')
        print(f'Mother is left with total coin amount of Rs{self.coins}/-.')
        print('--------------------------------')
    
class daughter(son,mother):
    ratio = 0.3
    def __init__(self,balance,cash,coins,mbalance,mcash,mcoins):
        # Here __init__ method of both the classes "son" & "mother" are called. Arguments are appropiately taken from child class __init__ method
        son.__init__(self,balance,cash,coins)
        mother.__init__(self,mbalance,mcash,mcoins)
        # Since class "daughter" is inheriting attributes of class "son" it will also inherit attributes of class "father". father --> son(father) --> daughter(son, father)
        self.dbalance = (daughter.ratio * self.balance) + (daughter.ratio * self.mbalance)
        self.dcash = (daughter.ratio * self.cash) + (daughter.ratio * self.mcash)
        self.dcoins = (daughter.ratio * self.coins) + (daughter.ratio * self.mcoins)
    def cash_display(self):
        print(f'Daughter has total bank balance amount of Rs{self.dbalance}/-.')
        print(f'Daughter has total cash amount of Rs{self.dcash}/-.')
        print(f'Daughter has total coin amount of Rs{self.dcoins}/-.')
        print('--------------------------------')
        self.balance = (1 - daughter.ratio - son.ratio) * self.balance
        self.cash = (1 - daughter.ratio - son.ratio) * self.cash
        self.coins = (1 - daughter.ratio - son.ratio) * self.coins
        print(f'Father is left with total bank balance amount of Rs{self.balance}/-.')
        print(f'Father is left with total cash amount of Rs{self.cash}/-.')
        print(f'Father is left with total coin amount of Rs{self.coins}/-.')
        print('--------------------------------')

s = son(20000,1000,500)
s.cash_display()

d = daughter(20000,1000,500,10000,500,300)
d.cash_display()
# :::Inheritance glitch discussion:::
son.cash_display(d)
mother.cash_display(d)

# :::check membership of a object instance for any class:::
# You can pass a tuple containing name of all class to check if a object instance belong to any of those classes
print(isinstance(d,(son,father)))
# Since class "daughter" is inheriting properties of class "son" & "daughter" therefore it is also an instance of class "son" & "daughter"
print(isinstance(s,daughter))
# Since class "son" is parent class of "daughter", it is not inheriting from it's class class. Therefore it's object instance cannot be an instance of class "daughter"
