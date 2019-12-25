from konlpy.tag import Komoran

kom = Komoran()

def pos_txt(txt_list):
    print('making pos_txt files', end="")
    for k in txt_list:
        f = open(k+'.txt', 'r', encoding='UTF8')
        rf = open(k+'_pos.txt', 'w', encoding='UTF8')
        text = f.read()
        text = text.split()
        pos_result = []
        for k in text:
            if k != '':
                if '<' not in k:
                    line = k + '\t'
                    pos = kom.pos(k)
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
    print('pos_txt process done')


test_list = ['C:/Users/USER/田유진/(수업) 자료전산처리방법론/파이썬 과제/newsreader/20191225/1632_02926',
        'C:/Users/USER/田유진/(수업) 자료전산처리방법론/파이썬 과제/newsreader/20191225/1632_00925']

if __name__=='__main__':
    pos_txt(test_list)

