import task_geturl
import re
import os
import sys
import urllib.request
from bs4 import BeautifulSoup

print('news files', end="")
for urls in task_geturl.link:
    url = urls
    html = urllib.request.urlopen(url)

    # making file and directory
    dir_name = url.strip('https://news.v.daum.net/v/')
    dir_name = 'C:/Users/USER/田유진/(수업) 자료전산처리방법론/파이썬 과제/newsreader/' + dir_name[:8]
    url_name = url[-9:]

    filename = dir_name + '/' + url_name + '.txt'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    f = open(filename, 'w', encoding='UTF8')

    # read contents
    bs_object = BeautifulSoup(html.read(), 'html.parser')
    title = bs_object.find('h3', {'class': "tit_view"})
    info = bs_object.find('span', {'class': 'info_view'})
    summary = bs_object.find('strong', {'class': 'summary_view'})

    news_head = [title, info, summary]

    # write head part
    f.write('<head>\n')
    for k in news_head:
        k = str(k)
        k = re.sub(r"<[^>]*>", " ", k)
        if k != 'None':
            k = k + '\n'
            f.write(k)

    # write body part
    body = bs_object.find_all('div', {'id': 'harmonyContainer'})

    body = str(body)
    body = body[1:len(body)-1]
    body = re.sub(r"<[^>]*>", " ", body)
    body = body.split(" ,  ")
    bodylist = list()
    for k in body:
        k.strip()
        bodylist.append(k)

    bodyresult = '\n\n'.join(bodylist)

    f.write('\n<body>')
    f.write(bodyresult)

    # finishing
    f.close()
    print(' +1', end="")

print('\nall process is done')
sys.exit()
