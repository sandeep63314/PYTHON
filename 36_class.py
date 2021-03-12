class _netflix:
    pass

print(f'Type of main class:',type(_netflix))
_tvshow = _netflix
print(f'Type of a variable after assigning it to a class type:',type(_tvshow))
_show = _tvshow()
print(type(_show))