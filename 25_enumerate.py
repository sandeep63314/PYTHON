# enumerate function returns index and value of an object in a tuple
for _lang in enumerate(('C++','C#','Python','Java')):
    print(_lang)

for _idx, _lang in enumerate(('C++','C#','Python','Java')):
    if _lang == 'Python':
        print(f'Index value of \'Python\' is {_idx}')