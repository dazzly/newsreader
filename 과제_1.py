import re
import urllib.request
from bs4 import BeautifulSoup

f = open('C:/Users/USER/田유진/(수업) 자료전산처리방법론/과제_1.txt', 'w')
test_url='https://news.v.daum.net/v/20191224150210126'
html = urllib.request.urlopen(test_url)
# print(type(html))

bs_object = BeautifulSoup(html.read(), 'html.parser')
head = bs_object.find('h3',{'class':"tit_view"})
info = bs_object.find('span',{'class':'info_view'})
summ = bs_object.find('strong', {'class':'summary_view'})
figc = bs_object.find_all('figcaption', {'class':'txt_caption default_figure'})
body = bs_object.find_all('p', {'dmcf-ptype':'general'})

news_head = [head, info, summ]
news_body = [figc, body]

for k in news_head:
    k = str(k)
    k = re.sub(r"<[^>]*>", " ", k)
    k = k + '\n'
    f.write(k)

figc = str(figc)

figc = re.sub(r"<[^>]*>", " ", figc)
figc = figc.split('           ')
figc = ''.join(figc)
f.write(figc)

body = str(body)
body = body[1:len(body)-1]
body = re.sub(r"<[^>]*>", " ", body)
body = body.split(" ,  ")
body = '\n\n'.join(body)
f.write(body)

# f.write(a)
f.close()
print('done')
