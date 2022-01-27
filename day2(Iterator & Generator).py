'''이터레이터(Iterator)
파이썬에서 반복자는 여러개의 요소를 가지는 컨테이너(리스트, 튜플, 셋, 사전, 문자열)에서 각 요소를
하나씩 꺼내 어떤 처리를 수행하는 간편한 방법을 제공하는 객체'''

for element in [1,2,3]:
    print(element)

for element in (1,2,3):
    print(element)

for element in {1,2,3}:
    print(element)

for key in {"a":1, "b":2, "c":3} :
    print(key)

for key, value in {"a":1, "b":2, "c":3}.items():
    print(key,value)

for char in "123":
    print(char)
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")

'''for문은 먼저 주어진 컨테이너 객체에 대해 iter() 메소드를 호출에서 이터레이터 객체를 구한다. 그리고
내부의 요소를 하나씩 가져오기 위해 __next__()를 호출. next 메소드는 하나의 요소를 반환하고 다음 요소를
가리킨다. 더이상 가져올게 없으면 StopIteration 예외를 발생시킴.'''
''' 터미널에서
s = 'abc'
it = iter(s)

next(it)
next(it)
next(it)
next(it)
'''

'''제너레이터(Generator)
제너레이터는 이터레이터를 만드는 간단하고 강력한 도구. 제너레이터는 일반적인 함수처럼 작성되지만
데이터를 반환하기 위해서 return 문장이 아니라 yield 문장을 사용함. 매번 next() 메서드가 호출될 때마다
제너레이터는 중단된 지점부터 다시 시작함.(모든 데이터 값과 마지막 실행된 명령문을 기억함.) 즉, return을
사용하는 함수라면, 반환될 때마다 내부 지역변수들은 사라지지만 yield 사용할 경우 내부 값들이 보존'''

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
#range(시작,끝, 간격) ex) range(1,11) 일때 1~10 나옴, 숫자의 간격에는 음수 지정 가능
for char in reverse('golf'):
    print(char)

'''제너레이터 표현식
함수의 인자로 즉시 사용되는 상황을 위해 디자인'''

sum(i*i for i in range(10))

print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")

'''itertools는 효율적인 루핑을 위한 이터레이터를 만드는 모듈. for...in 반복문에서 이터레이터 함수를 호출할 때
함수는 한 번에 한 항목을 반환하고 호출 상태를 기억
chain 함수는 순회가능한 인수들을 차례로 반복'''

import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

shu = (['관우', '장비', '조운', '마초', '황충', '위연'], ['제갈량', '방통', '서서', '강유', '법정', '마량'])
wei = (['하후돈', '장료', '서황', '우금', '악진', '장합'], ['사마의', '순욱', '순유', '곽가', '가후', '정욱'])
wu = (['정보', '황개', '한당', '주태', '감녕', '태사자'], ['주유', '노숙', '여몽', '육손', '제갈근', '장소'])

tot = list(itertools.chain(*shu, *wei, *wu))
#별표 문법(asterisk/star syntax) : 각 튜플들을 풀어 해침
print(tot)

#cycle 인수를 순환하는 이터레이터 
#for item in itertools.cycle([1, 2]):
#    print(item)

#accumulate() 축적된 값 계산. 기본으로 합계 계산
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

def multiply(a,b):
    return a * b

#두번째 인수로 함수 사용 가능. 여기서는 축적된 곱
for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)