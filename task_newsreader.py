import re
import urllib.request
from bs4 import BeautifulSoup


test_url='https://news.v.daum.net/v/20191224150210126'
html = urllib.request.urlopen(test_url)

urlname = test_url[-6:-1]

f = open(urlname+'.txt', 'w', encoding='UTF8')


bs_object = BeautifulSoup(html.read(), 'html.parser')
head = bs_object.find('h3',{'class':"tit_view"})
info = bs_object.find('span',{'class':'info_view'})
summ = bs_object.find('strong', {'class':'summary_view'})


news_head = [head, info, summ]

for k in news_head:
    k = str(k)
    k = re.sub(r"<[^>]*>", " ", k)
    k = k + '\n'
    f.write(k)

# figc = bs_object.find_all('figcaption', {'class':'txt_caption default_figure'})
# figc = str(figc)
#
# figc = re.sub(r"<[^>]*>", " ", figc)
# figc = figc.split('           ')
# figc = ''.join(figc)
# # f.write(figc)
# print(figc)

# bs_object.find_all((re.compile("p|div"), {'dmcf-ptype':'general'}))
body = bs_object.find_all('div', {'id':'harmonyContainer'})


body = str(body)
body = body[1:len(body)-1]
body = re.sub(r"<[^>]*>", " ", body)
body = body.split(" ,  ")
bodylist = list()
for k in body:
    k.strip()
    bodylist.append(k)

bodyresult = '\n\n'.join(bodylist)

f.write(bodyresult)
# print(bodyresult)

# f.write(a)
f.close()
print('done')
