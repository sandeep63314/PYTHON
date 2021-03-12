ticket = {2: {'Honda Activa': 5, 'Suzuki Gixer': 3, 'Bajaj Pulsar': 7},
          3: {'Piagio': 5},
          4: {'TATA Nano': 3, 'Hyundai Verna': 5, 'Renault': 3}}
# If a key value pair doesn't exist in dictionary and we want to access it then it will return keyError
# To mitigate this issue we need to use get()
# get() solves this error by initializing the key to a default value if it doesn't exist.
# If default value is not supplied then key will return 'None'
# get() allows you to set a default value to a key if it doesn't exist
print(ticket.get(4).get('Maruti Suzuki'))
print(ticket.get(4).get('Maruti Suzuki',6))
#print(ticket)

# Other way to create a dictionary and assign it to a variable is by using dict function
# Note you cannot assign any number as a key here. Do not enclose the key in single quotes
ticket2 = dict(_2wheeler=dict(HondaActiva=5, SuzukiGixer=3, BajajPulsar=7))
print(ticket2['_2wheeler']['BajajPulsar'])

# pop() is used to pop a given item based on key.
# It returns corresponding value of a key
print(ticket[2].pop('Bajaj Pulsar'))
print(ticket)

# popitem is used to randomly pop any item. Most of the time it pops up the last item
print(ticket.get(4).popitem())

# Update a given key in dictionary
# If the key is present then it will update it's value
# If that key is not present then it will add the given key value pair
ticket[2].update({'Suzuki Gixer': 4})
ticket[2].update({'Bajaj Pulsar': 6})
ticket[2].update({'TVS Apache': 7})
print(ticket)

# Another way to add a item into dictionary is by using setdefault()
ticket[3].setdefault('Tricycles', 2)
print(ticket)

# To retrieve all keys from dictionary
print(ticket.keys())

# To retrieve all values from dictionary
print(ticket.values())

# item() is used to retrieve key value pairs from dictionary
# key value pairs are collected into tuples
print(ticket.items())

# To remove all items from dictionary
ticket.clear()
print(ticket)