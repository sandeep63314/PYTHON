# Dictionary is a unordered collection of key and value pair
ticket = {2: {'Honda Activa': 5, 'Suzuki Gixer': 3, 'Bajaj Pulsar': 7},
          3: {'Piagio': 5},
          4: {'TATA Nano': 3, 'Hyundai Verna': 5, 'Renault': 3}}
print(ticket)
# A key in dictionary has to be unique. Duplicate keys will return keyvalue error
# To get the value we need to mention the index value in dictionary object
print(ticket[4]['Hyundai Verna'])