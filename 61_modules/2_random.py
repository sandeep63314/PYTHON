import random

# random() * 100 : Randomly select a number less than 100. random() generates a decimal number between 0 and 1
print(int(random.random() * 100))

# randint() : Randomly select a number starting from 1 and ending at 10
print(random.randint(1, 10))

# choice() : Randomly select a item from a collection
winners = ['Anurag', 'Sambit', 'Avinash', 'Sampad', 'Gaurav']
print(random.choice(winners))

# shuffle() : Randomly change index position of items in a collection
random.shuffle(winners)
print(winners)
