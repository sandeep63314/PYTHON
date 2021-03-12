# args(arguments) is a parameter that accepts any number of argument values
# kwargs(keyword arguments) is a parameter that accepts a dictionary
#params, *args, default arguments, **kwargs
def stock_price(name,*price,**day_price):# it is a standard convention to use *args, **kwargs as name of argument & keyword arguments
    print(day_price)
    print(price)
    total = 0
    for amount in day_price.values():
        total += amount
    total +=sum(price)
    length = len(price) + len(day_price.keys())
    return total/length

print(f"Average price of Petrol in this weekend is {stock_price('Petrol',80,80.5,81.20,82,fri = 81.5,sat = 80.70,sun = 81)}")
