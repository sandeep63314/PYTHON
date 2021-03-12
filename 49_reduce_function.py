from functools import reduce

# Unlike other functions map, filter and zip, reduce function is not an inbuilt function in python.
# This function works on all items inside an iterable and returns a single value
EMI = [11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000,
       11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000, 11000]

cntr = 0


def calculate_amount(amount, emi, roi=7):
    global cntr
    cntr += 1
    # Every time amount value is calculated as amount = amount + emi if (cntr % 12) != 0
    if (cntr % 12) != 0:
        return amount + emi
    else:
        return (((100 + roi) / 100) * (amount + emi))


# 0 is the initial value of the amount that is going to be returned after working with each values in an iterable.
total = reduce(calculate_amount, EMI, 0)
cntr = cntr / 12
print(f'Total amount after paying sum of Rs {EMI[0]}/- for {cntr} years is Rs {total}/-')