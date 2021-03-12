# removing duplicates from a list
_some_list = ['a','b','c','b','d','m','n','n']
_uq_list = []

for _item in _some_list:
    if _item not in _uq_list:
        _uq_list.append(_item)
    else:
        continue
print(_uq_list)