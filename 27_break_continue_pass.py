# break statement is used to come out of the loop based on a certain criteria
# continue statement is used to return back to the loop condition based a certain criteria
# pass statement simply moves to the next statement execution

_veg = {'cucumber': 50, 'brinjal': 50, 'tomato': 70, 'saag':20}

for _item,_price in _veg.items():
    if _item in ['tomato','saag','brinjal']:
        continue # execution will return back to the loop if item in ['tomato','saag','brinjal']
    elif _item in ['cucumber']:
        _itm = _item
        _prc = _price + 10
        _veg.update({_itm:_prc})
        break # execution will come out of the loop once item = 'cucumber'
pass # simply allows you to execute next statement without any criteria. This is used to write a block of code in future
print(_veg)