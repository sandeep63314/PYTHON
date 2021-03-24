usernames = ['sangram','sandeep','sanjay','sambit','sanjay','sangram','Rahul','sandeep','sandeep','sangram','sanjay','sandeep']
usernames.sort()
print(usernames)
ctr = 0
while ctr < len(usernames) - 1:
    if usernames[ctr] == usernames[ctr+1]:
        usernames.pop(ctr) # pop a given item if it is matching with next item
    else:
        ctr += 1 # ctr is incremented if successive items are not matching
print(usernames)