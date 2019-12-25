from konlpy.tag import Komoran

kom = Komoran()


def pos_txt(txt_list):
    print('making pos_txt files', end="")
    for k in txt_list:
        f = open(k+'.txt', 'r', encoding='UTF8')
        rf = open(k+'_pos.txt', 'w', encoding='UTF8')  # result file
        text = f.read()
        text = text.split()
        for word in text:
            if word != '':
                if '<' not in word:  # tag가 아닌 것만 분석
                    line = word + '\t'  # 이하 분석 결과를 가독성 있게 한 줄에 작성
                    pos = kom.pos(word)
                    for n in range(len(pos)):
                        token = pos[n]
                        pos_token = " " + token[0] + '/' + token[1]
                        line += pos_token
                        if n != len(pos)-1:
                            line += ' + '
                        else:
                            line += '\n'
                    rf.write(line)

        f.close()
        rf.close()
        print(' +1', end="")
    print('\npos_txt process done')


# for check
test_list = ['C:/Users/USER/newsreader/20191225/1632_02926', 'C:/Users/USER/newsreader/20191225/1632_00925']

if __name__ == '__main__':
    pos_txt(test_list)
