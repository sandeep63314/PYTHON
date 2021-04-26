import datetime
_curr_year = datetime.date.today()
_curr_year = _curr_year.strftime('%Y')
print(_curr_year)
_birth_year = input('Enter your year of birth:')
# Type conversion from string to integer
_age = int(_curr_year) - int(_birth_year)
print(f'You are {_age} years old.')