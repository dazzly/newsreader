import urllib.request
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews'
html = urllib.request.urlopen(url)
bs_object = BeautifulSoup(html.read(), 'html.parser')

# bs_object.find('div', {'class': 'legal-container'}).decompose()

main = bs_object.find_all('div', {'class':'box_etc'})
print(type(main))

link = []
for k in main:
    tags = k.find_all("a", {"class": "link_txt"})
    for i in tags:
        link.append(i['href'])
print(link)