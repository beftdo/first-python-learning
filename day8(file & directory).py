'''Folder = Directory
File System -> Tree

open() 
기존 파일 읽기
새 파일 쓰기
기존 파일에 추가하기
기존 파일 덮어쓰기

fileobj = open(filename, mode)
fileobj : 반환되는 파일 객체
filename : 파일의 문자열 이름
mode : 파일 타입과 파일로 무엇을 할지 명시
rwxa(add) / t(txt type), b(binary type)
파일을 열고 다 사용했다면, 사용한 메모리를 해제하기 위해 파일을 닫아야 한다.'''

fout = open('oops.txt', 'wt')
fout.close()

fout = open('oops.txt', 'wt')
print('Oops, I created a file.' , file=fout)
#file 옵션이 없다면 터미널인 표준 출력에 내용을 쓴다
fout.close

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

print(len(poem))
fout = open('relativity', 'wt')
fout.write(poem)
fout.close

'''fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close'''
'''print() 각 인수 뒤에 스페이스를, 끝에 줄바꿈을 추가한다.'''

'''fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()'''

'''
fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close
'''

'''try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')'''

# read() 함수를 인수 없이 호출하여 한 번에 파일 전체 내용을 읽을 수 있다.
# 대형 파일로 이 작업을 수행 시 많은 메모리가 소비
fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))

# read() 함수가 한 번에 읽을 수 있는 문자 수를 제한하려면 최대 문자 수를 인수로 입력
poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += len(fragment)
fin.close()
print(len(poem))

#readline() 함수는 read() 함수처럼 파일 끝에 도달 했을 때, False로 간주하는 빈 문자열을 반환한다.
poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))

#텍스트 파일을 가장 읽기 쉬운 방법은 이터레이터를 사용하는 것이다.
#이터레이터는 한 번에 한 줄씩 반환한다.
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
print(len(poem))

fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')

print("---------------------------------------------------------------------")
#이진 파일 쓰기

bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
fout.close()

fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()
print("---------------------------------------------------------------------")

'''
열려 있는 파일을 닫지 않았을 때, python은 이 파일이 더 이상 참조되지 않는 것을 확인한 뒤 파일을 닫는다.
이것은 함수 안에 파일을 열어놓고 이를 명시적으로 닫지 않아도 함수가 끝날 때 자동으로 파일이 닫힌다는 것
그러나 오랫동안 작동하는 함수 or 메인 프로그램에 파일을 열어 놓았다면, 마지막으로 파일을 닫아야한다.

컨택스트 매니저(context manager) : 파일을 여는 것과 같은 일을 수행
컨텍스트 매니저 코드 블록의 코드 한 줄이 실행되고 나서 자동으로 파일을 닫아준다.
'''
with open('relativity', 'wt') as fout:
    fout.write(poem)

# tell() 함수는 파일 시작 위치에서 현재 오프셋을 바이트 단위로 반환.
fin = open('bfile', 'rb')
print(fin.tell())
# seek() 함수를 사용하여 파일의 마지막에서 1바이트 전 위치로 이동한다.
print(fin.seek(255))

bdata = fin.read()
print(len(bdata))
print(bdata[0])

'''
seek(offset, origin)
origin이 0일때(기본값), 시작 위치에서 offset 바이트로 이동환다.
origin이 1일 때, 현재 위치에서 offset 바이트로 이동한다.
origin이 2일 때, 마지막 위치에서 offset 전 위치로 이동한다.
'''

import os
print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)

fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin = open('bfile', 'rb')
fin.seek(254, 0)
fin.tell()

fin.seek(1,1)
fin.tell()
bdata = fin.read()
print(len(bdata))
print(bdata[0])

print("---------------------------------------------------------------------")
#파일 혹은 디렉터리가 실제로 존재하는지 확인
import os
print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))
print(os.path.exists('..'))

#유형 확인하기
name = 'oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isdir('.'))

#isabs() 절대경로인지 확인
print(os.path.isabs(name))
print(os.path.isabs('/big/fake/name'))
print(os.path.isabs('big/fake/name/without/a/leadign/slash'))

#copy
import shutil
shutil.copy('oops.txt', 'ohno.txt')
#shutil.move() 함수는 파일을 복사한 후 원본 파일을 삭제한다.

import os
os.rename('ohno.txt', 'ohwell.txt')

#link() 하드 링크 생성 , symlink() 심볼릭 링크 생성, islink() 파일이 심볼릭 링크인지 확인
os.link('oops.txt', 'yikes.txt')
print(os.path.isfile('yikes.txt'))
print(os.path.islink('yikes.txt'))

#os.symlink('oops.txt','jeepers.txt')
#print(os.path.islink('jeepers.txt'))

#권한 바꾸기
os.chmod('oops.txt', 0o400)

import stat
os.chmod('oops.txt', stat.S_IRUSR)

'''uid = 5
gid = 22
os.chown('oops', uid, gid)'''

os.remove('oops.txt')
print(os.path.exists('oops.txt'))