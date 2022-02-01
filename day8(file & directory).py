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
'''fout = open('relativity', 'wt')
fout.write(poem)
fout.close'''

'''fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close'''
'''print() 각 인수 뒤에 스페이스를, 끝에 줄바꿈을 추가한다.'''

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

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

try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')