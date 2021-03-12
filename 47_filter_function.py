# Filter function is used to filter a list of values from a collection

# The filtered values can be a list, tuple or a set

users = ['Sangram', 'Srikant', 'Lipika', 'Rajan', 'Subhashree', 'Bighnaraj']


def check_users(users):
    return users[0] == 'S'


userS = list(filter(check_users, users))
print(userS)
# ---------------------------------------------------------------
ch_price = {'ten sports': 19, 'otv': 0, 'HBO': 10, 'nat geo': 5, 'DD news': 0}
channels = list(ch_price.keys())


def zero_price(ch):
    return ch_price[ch] != 0


zero_ch = list(filter(zero_price, channels))
print(zero_ch)