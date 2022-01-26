'''자료구조는 자료를 효율적으로 접근하고 수정하기 위해 자료를 조직, 관리, 저장하는 방법 의미
상황에 따라 데이터를 다루는데 시간과 메모리를 효율적을 사용하기 위해서 필요

선형 자료 구조 : 자료를 구성하는 데이터들이 직선 형태로 순차적을 나열, 전후 데이터들 간 1:1 관계
비선형 자료 구조 : 하나의 자료 뒤에 여러개의 자료가 존재할 수 있음. 전후 데이터들 간 1:N 관계

선형 자료 구조 : Stack, Queue,Deque ,List
비선형 자료 구조 : Tree, Graph 등

스택은 한 쪽 끝에서만 데이터를 넣거나 뺄 수 있는 후입 선출(Last In First Out, LIFO) 자료구조 ex)하노이의 탑
큐는 한 쪽 끝에서 데이터가 삽입되고, 다른 한 쪽 끝으로 삭제된느 선입 선출(First In First Out, FIFO)의
자료구조.
데크는 스택과 큐의 기능을 모두 가진 출입구가 양 끝에 있는 큐다. 양쪽 끝에서 데이터들을 넣고 뺄 수 있다.

자료구조에서 데이터를 넣는 작업을 push, 자료를 꺼내는 작업을 pop이라고 한다.
palindrome(화문) : 앞에서부터 읽으나 뒤에서부터 읽으나 같은 구문
'''

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))
print("---------------------------------------------------------------------")

def another_palindrome(word):
    return word == word[::-1]

if another_palindrome('radar'):
    print("True")
else : print(False)

if another_palindrome('halibut'):
    print("True")
else : print(False)
