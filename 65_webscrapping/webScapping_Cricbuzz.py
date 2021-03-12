import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.cricbuzz.com')
page = BeautifulSoup(req.text,'html.parser')

getid = page.find(id = 'hm-scag-mtch-blk')
#getclass = page.select('.cb-col cb-col-100 videos-carousal-wrapper')

getli = getid.find_all('li')

for idx,li in enumerate(getli):
    print('~~~~~')
    getdiv = getli[idx].find('a').find_all('div')
    for div in getdiv:
        innerdivs = div.find_all('div')
        i = 0
        text = ''
        for divs in innerdivs:
            i += 1
            text += divs.getText() + ' '
            if (i == 2):
                print(text)
        i = 0

