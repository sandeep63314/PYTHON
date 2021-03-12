import requests
from bs4 import BeautifulSoup

req = requests.get('https://timesofindia.indiatimes.com/news')
formattedtext = BeautifulSoup(req.text, 'html.parser')

# find_all() is used to grab all occurences of a tag/element in a list
findall = formattedtext.find_all('div')

# find() is used to grab a particular attribute(#id) or tag. It only grabs the first occurence
findtag = formattedtext.find(id="ulItemContainer")

# for _ in findall:
#     print('~~~~~')
#     print(_)

# print(findtag)

# select() is used to grab all occurrences of an attribute into a list
select = formattedtext.select('.w_tle')

# for _ in select:
#     print('~~~~~')
#     print(_)

# for span in select:
#     print('~~~~~')
#     gettext = span.find('a').getText()
#     print(gettext)

for span in select:
    print('~~~~~')
    gettitle = span.find('a').get('title')
    gethref = span.find('a').get('href')
    print(gettitle + ' , ' + ('https://timesofindia.indiatimes.com'+gethref if gethref[0] == '/' else gethref))