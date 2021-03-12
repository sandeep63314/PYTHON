class billcounter:
    packing = 15

    def __init__(self, _discount, _charges):
        #It is not mandatory that attributes and __init__ function parameters should be of same name
        #Only class attributes are called using 'self' keyword
        self.discount = _discount
        self.charges = _charges

    def calculate_bill(self, totalbill, distance):
        if int(distance) < 5:
            self.charges = self.charges
        elif 5 <= int(distance) < 10:
            self.charges += 10
        elif 10 <= int(distance) < 15:
            self.charges += 20
        else:
            self.charges += 30

        finalbill = (((100 - self.discount) / 100) * float(totalbill)) + billcounter.packing + self.charges
        return finalbill

    @classmethod
    # @classmethod are used to override values of class attributes
    # Like functions defined inside class, @classmethod has a 'cls' parameter to call it's own parameter
    # 'cls' parameter inside @classmethod is also used to override values of class attributes
    def discount_bill(cls):
        # Here cls is used to assign 50 to discount and 10 to charges.
        return cls(50, 10)


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for ctr, today in enumerate(days):
    print(ctr + 1, today)
weekday = input('Choose your desired weekday from above:')
total = input('Enter the total amount:')
delivery = input('Enter the total distance to be travelled:')

if weekday == 'Wed':
    billdesk = billcounter.discount_bill()
    finalamount = billdesk.calculate_bill(total, delivery)
else:
    billdesk = billcounter(25, 20)
    finalamount = billdesk.calculate_bill(total, delivery)

print(f'Your final amount is Rs {finalamount}/-')
print('Enjoy your meal :) :) :)')
