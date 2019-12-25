import geturl
import txt_konlpy
import re
import os
import sys
import urllib.request
from bs4 import BeautifulSoup

print("Daum 뉴스에서 '최신 뉴스'의 첫 페이지에 있는 모든 뉴스를 txt 파일로 가져옵니다")
print('news files', end="")
result_files = []

for urls in geturl.link:
    url = urls
    html = urllib.request.urlopen(url)

    # making file and directory
    dir_name = url.strip('https://news.v.daum.net/v/')
    dir_name = 'C:/Users/USER/newsreader/' + dir_name[:8]
    url_name = url[-9:-5] + '_' + url[-5:]

    filename = dir_name + '/' + url_name
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    result_files.append(filename)

    f = open(filename+'.txt', 'w', encoding='UTF8')

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
n = int(input('각 파일에 대한 형태소 분석을 하시려면 1을, 이대로 종료하려면 0을 입력해주세요: '))
if n == 1:
    txt_konlpy.pos_txt(result_files)
elif n == 0:
    print('프로그램을 마칩니다.')
    sys.exit()
else:
    print('Invalid input, terminate process')
sys.exit()
