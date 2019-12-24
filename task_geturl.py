import urllib.request
from bs4 import BeautifulSoup

# page of newest news
url = 'https://news.daum.net/breakingnews'
html = urllib.request.urlopen(url)
bs_object = BeautifulSoup(html.read(), 'html.parser')

# get main news list
main = bs_object.find_all('div', {'class':'box_etc'})
print(type(main))

# get links of news
link = []
for k in main:
    tags = k.find_all("a", {"class": "link_txt"})
    for i in tags:
        link.append(i['href'])
print('getting link is done')  # for check
