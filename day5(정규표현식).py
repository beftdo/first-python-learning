'''정규표현식 regular expression
복잡한 문자열 패턴 매칭 가능, 표준 모듈 re
원하는 문자열 패턴을 정의하여 소스 문자열과 일치하는지 비교'''
import re
result = re.match('You', 'Young Frankenstein')
print(result)
#You는 패턴, Young Frankenstein은 확인하고자 하는 문자열 소스
#match()는 패턴의 일치 여부 확인

#나중에 패턴 확인 빠르게 하기 위해 패턴부터 컴파일 하는 방법
yourpatttern = re.compile('You')
result = yourpatttern.match('Young Frankenstein')
#컴파일 된 패턴으로 일치여부 확인
print(result)

'''
match()는 소스 첨부터 시작하는 패턴만 매칭
search()는 소스 어디서나 패턴 찾아 매칭, 첫 번째 일치하는 항목 반환
findall()은 중첩에 상관없이 패턴에 일치하는 모든 문자열 리스트 반환
split() 패턴에 맞게 소스를 쪼갠 후 문자열 조각의 리스트 반환
sub() 대체 인수를 하나 더 받아서, 패턴에 일치하는 모든 소스 부분을 대체 인수로 변경
'''

source = 'Young Frankenstein'
m = re.match('You', source)
if m: #match는 객체 반환. 무엇이 일치하는지
    print(m.group())

source = 'Young Frankenstein'
m = re.match('^You', source) #맨 앞자리에 ^가 있어도 You 반환
if m:
    print(m.group())
print("---------------------------------------------------------------------")

source = 'Young Frankenstein'
m = re.match('Frank', source)
if m:
    print(m.group()) 

#match가 아무것도 반환하지 않아서 print()가 실행되지 않음.
#:= 연산자를 사용해서 줄임

source = 'Young Frankenstein'
if m := re.match('Frank', source):
    print(m.group())

source = 'Young Frankenstein'
m = re.search('Frank', source) #패턴이 어느 위치에 있더라도 동작
if m:
    print(m.group())

source = 'Young Frankenstein'
m = re.match('.*Frank', source)
# .은 한 문자 의미
# *은 바로앞의 패턴이 무한대로 반복 될 수 있다는 의미. *는 0회 이상의 문자가 올 수 있다는 것
if m:
    print(m.group())
print("---------------------------------------------------------------------")

source = 'Young Frankenstein'
m = re.findall('n', source)
print(m) #findall은 결과값을 리스트로 반환
print('Found', len(m), 'matches')

source = 'Young Frankenstein'
m = re.findall('n.', source) #n다음에 오는 한 문자
print(m)

source = 'Young Frankenstein'
m = re.findall('n.?', source) #n 이후에 선택적으로 다음 문자가 올 수 있도록 ? 추가
#?는 0 또는 1회를 의미, 하나의 문자가 0또는 1회 올 수 있다.
print(m)
print("---------------------------------------------------------------------")

source = 'Young Frankenstein'
m = re.split('n', source)
print(m) #split()은 패턴 앞뒤로 소스를 나눠서, 리스트 반환

source = 'Young Frankenstein'
m = re.sub('n', '?', source)
print(m) #sub는 문자열 반환, 첫번째 인수를 두번째 인수로 대체
#replace() 메서드와 비슷하지만, 리터럴 문자열이 아닌 패턴 사용

print("---------------------------------------------------------------------")
#string 모듈은 테스트에 사용할 수 있는 문자열 상수가 미리 정의되어 있다.
import string
printable = string.printable
print(len(printable))
print(printable[0:100])

# 메타 문자(meta charactes): 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자

print(re.findall('\d', printable)) #\d 숫자
print(re.findall('\w', printable)) #\w 문자 + 숫자
print(re.findall('\s', printable)) #\s 공백문자
#결과값 순서대로 스페이스, 탭, 줄바꿈, 캐리지 리턴, 세로 탭 및 폼 피드
print("---------------------------------------------------------------------")

#정규 표현식은 아스키 코드에만 국한되지 않는다.
x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(x)
print(re.findall('\w', x))
print("---------------------------------------------------------------------")

#패턴 지정자
source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''
print(re.findall('wish',source))
print(re.findall('wish|fish',source))
print(re.findall('^wish', source))
print(re.findall('^I wish', source)) #^은 소스 문자열 시작 패턴 지정자
print(re.findall('fish$', source)) #$은 소스 문자열 끝 패턴 지정자
print(re.findall('fish tonight.$', source)) #$은 소스 문자열 끝 패턴 지정자
#정확하게 문자 그대로 매칭하기 위해서는 .에 이스케이프 문자를 붙여야 함 .은 \n을 제외한 모든 문자기 때문
print(re.findall('fish tonight\.$', source))
print(re.findall('[wf]ish', source)) #[abc] a 또는 b 또는 c = a|b|c
print(re.findall('[wsh]+', source)) #prev +는 하나 이상을 패턴 의미, wsh 중 하나 이상 붙어있는 문자열 찾음
print(re.findall('ght\W', source)) #\W는 알파벳 문자가 아닌것
print(re.findall('I (?=wish)', source)) # prev(?=next) 뒤에 next가 오는 prev / 뒤에 wish가 오는 I
print(re.findall('(?<=I) wish', source)) # (?<=prev) next  앞에 prev가 오는 next 찾음

#정규 표현식 패턴이 파이썬 문자열 규칙과 충돌하는 경우
print(re.findall('\bfish', source))
# 파이썬 문자열에서는 \b는 백스페이스이지만, 정규 표현식에서는 \b는 단어의 경계 부문을 의미
# 정규 표현식을 시작할 때 r을 입력하면 해결 -> 이스케이프 문자를 사용하지 못하게 됨.
print(re.findall(r'\bfish', source))

#패턴을 괄호로 둘러싸면 매칭은 그 괄호만의 그룹으로 저장
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
# (?P<name> expr) 패턴을 사용하면, 표현식(expr)이 매칭되고, 그룹 이름(name)이 매칭
print(m.group())
print(m.group('DISH'))
print(m.group('FISH'))


print("---------------------------------------------------------------------")
#연습문제
mammoth = '''We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.[Pg 72]
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.'''

import re
print(re.findall(r'\bc\w*' , mammoth))
#\b는 단어와 비단어 사이의 경계의 시작을 의미. 단어의 시작이나 끝을 지정하기 위해 \b 사용
print(re.findall(r'\bc\w{3}\b' , mammoth))
#단어의 끝을 표시하기 위해 마지막에 \b사용. 마지막 \b를 빼면 c로 시작하는 네글자 이상의 모든 단어 중
#처음 네 글자가 다 검색됨 ex)cheese -> chee
print(re.findall(r'\b\w*r\b' , mammoth))
print(re.findall(r'\b\w*l\b', mammoth))
#\w 패턴은 작은따옴표를 제외한 문자, 숫자 언더바만 매칭하기 때문에 정확하다고 보기 힘듦
print(re.findall(r'\b[\w\']*l\b', mammoth)) #이스케이프 문자 아니면 큰따옴표 사용
print(re.findall(r"\b[\w']*l\b", mammoth))
print(re.findall(r'\b\w*[aeiou]{3}[^aeiou]*\w*\b' , mammoth))
#\w*는 0회 이상이기 때문에 있을 수도 없을 수도 있음. 비모음 문자를 단어의 끝에 넣기 위해
#[^aeiou] 사용. 하지만 beau\nIn 출력. 줄바꿈 문자 제외 필요 + 공백문자
print(re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b' , mammoth))
