import os
os.mkdir('poems')
os.path.exists('poems')

os.rmdir('poems')
os.path.exists('poems')

os.mkdir('poems')
os.listdir('poems')

os.mkdir('poems/mcintyre')
os.listdir('poems')

fout = open('poems/mcintyre/the_good_man', 'wt')
fout.write('Cheerful and happy was his mood,He to the poor was kind and good.')
fout.close()
os.listdir('poems/mcintyre')

import os
os.chdir('poems')
os.listdir('.')
print("---------------------------------------------------------------------")

#glob() : 유닉스 셸 규칙을 사용하여 일치하는 파일이나 디렉터리 이름을 검색해 줌.
import glob
print(glob.glob('m*'))
print(glob.glob('??'))
print(glob.glob('m??????e'))
print(glob.glob('[klm]*e'))

#유닉스와 macOS 웹 주소는 경로 구분 기호로 슬래시를 사용하고 윈도우는 백슬래시를 사용한다.
#abspath() 절대경로 얻기 / realpath() 심볼릭 링크의 real 경로 얻기
print(os.path.abspath('oops.txt'))

#연습문제
import os
print(os.listdir('..'))
print(os.listdir('../..'))

test = 'This is a test of the emergency text system'
with open('test.txt', 'wt') as fout:
    fout.write(test)

with open('test.txt', 'rt') as fout:
    print(fout.read())