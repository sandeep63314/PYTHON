import pandas

read_csv = pandas.read_csv('grocery.csv')

print(read_csv) # print contents of a csv file
print(f'Total number of rows in grocery.csv file is {len(read_csv)}') # print total number of rows in a csv file
print(read_csv['date_of_purchase'].loc[0:3]) # print rows of a particular file. You can specify start and end index values of rows
print(dict(read_csv.loc[1:3])) # print rows from start and end index values of rows