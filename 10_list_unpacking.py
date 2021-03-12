# Unpacking values in a list and assigning to variables
# Let 10 values be assigned to 3 variables.
# First 2 values are assigned to first 2 variables.
# Next 8 values are collected into a list and assigned to 3rd variable

_id, _name, _project, *_emp_details, _designation = [705306, 'Sangram Mohanty', 'Shell', 3.5, '20-08-2015',
                                                     '25-01-2020', 'Senior Associate']
print(_id)
print(_name)
print(_project)
print(_emp_details)
print(_designation)

_experience, _doj, _dol = _emp_details
print(_experience)
print(_doj)
print(_dol)
