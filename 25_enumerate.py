# enumerate function returns index and value of an object in a tuple
languages = ('C++','C#','Python','Java')
l = enumerate(languages,1)
print(l)

for _lang in enumerate(languages):
    print(_lang)

for _idx, _lang in enumerate(('C++','C#','Python','Java'),1):
    if _lang == 'Python':
        print(f'Rank of \'Python\' is {_idx}')