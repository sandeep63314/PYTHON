_name = 'Sangram'
_dob = '18/11/1992'
_city = 'Bhubaneswar'
# Creating a formatted string
_details = f'''
Name:{_name}
DateOfBirth:{_dob}
City:{_city}'''
print(_details)
# Using the format function to specify position of arguments in string
_details = '''
Name:{2}
DateOfBirth:{1}
City:{0}'''
print(_details.format(_name, _dob, _city))
# Using the format function to create new variables passed as parameters
_details = '''
Name:{_newname}
DateOfBirth:{_newdob}
City:{_newcity}'''
print(_details.format(_newname='Sandeep', _newdob='24/12/2003', _newcity='Kolkata'))
