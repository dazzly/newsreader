import re
import urllib.request
from bs4 import BeautifulSoup


test_url='https://news.v.daum.net/v/20191224215601536'
html = urllib.request.urlopen(test_url)

urlname = test_url[-5:]

f = open(urlname+'.txt', 'w', encoding='UTF8')


bs_object = BeautifulSoup(html.read(), 'html.parser')
title = bs_object.find('h3',{'class':"tit_view"})
info = bs_object.find('span',{'class':'info_view'})
summary = bs_object.find('strong', {'class':'summary_view'})


news_head = [title, info, summary]

f.write('\n<head>\n')
for k in news_head:
    k = str(k)
    k = re.sub(r"<[^>]*>", " ", k)
    k = k + '\n'
    f.write(k)


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

f.write('\n<body>\n')
f.write(bodyresult)


f.close()
print('done')
