from functools import reduce

# set comprehension is similar to list comprehension
# set comprehension returns a set after action over all elements in a collection.
duplicates = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

check_duplicates = list({item for item in duplicates if duplicates.count(item) > 1})

print('Duplicate items in the list: -')
print(check_duplicates)

def decript(acc, passwd):
    return acc + chr(passwd)


# dictionary comprehension works on keys & values of a dictionary.
# You can perform actions on either keys or values of a dictionary and return them as a dictionary using dictionary comprehension.
encrypt_pass = {'mohanty': [68, 45, 76, 114, 95], 'sanjay': [67, 23, 56, 78, 122], 'sangram': [75, 81, 117, 50, 93]}

# Action was performed over each values of a dictionary
decrypt_pass = {user: reduce(decript, passwd, '') for user, passwd in encrypt_pass.items()}
# decript_pass = {user: reduce(lambda acc,x : acc + chr(x), passwd, '') for user, passwd in encript_pass.items()}

print('\nList containing userids and their decrypted passwords: -')
print(list(decrypt_pass.items()))