# Zip is used to create a tuple from each item mentioned in iterables
# It's like zipping each value from all tupless

users = ['Sangram', 'Srikant', 'Lipika', 'Rajan', 'Subhashree', 'Bighnaraj','Sridev']

phone_number = [9090403020, 9040102030, 986512345, 8917645671, 6371078910, 993787654]

# It had zipped each user with their phone numbers. However, user 'Sridev' couldn't be zipped.
# User 'Sridev' is missing his corresponding phone number from list
print(list(zip(users, phone_number)))
