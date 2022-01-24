'''파이썬 3의 문자열은 바이트 배열이 아닌 유니코드 문자 시퀀스다
파이썬의 unicodedata 모듈은 유니코드 식별자와 이름으로 검색할 수 있는 함수를 제공한다
lookup() : 인수로 대소 문자를 구분하지 않는 이름을 취하고, 유니코드 문자를 반환한다
name() : 인수로 유니코드 문자를 취하고, 대문자 이름을 반환한다'''

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' %(value, name, value2))
#인수를 유니코드 값으로 반환 후, 다시 그 유니코드 값을 대문자로 반환

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')
print("---------------------------------------------------------------------")

'''é를 유니코드 문자 이름 인덱스에서 찾으면 E WITH ACUTE, LATIN SMALL LETTER
로 나오는데 파이썬에서 사용하는 유니코드 이름으로 바꾸려면 콤마 뒤에 오는 단어를 앞으로 
옮기고 원래 콤마 앞에 있던 단어를 뒤로 옮겨야 한다. 바꾸면 LATIN SMALL LETTER E WITH ACUTE
''' 
import unicodedata
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))
print(unicodedata.name('é'))

u_umlant = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlant)

#문자열 len() 함수는 유니코드의 바이트가 아닌 문자수를 센다.
print(len('$'))
print(len('\u2603'))

#유니코드의 숫자 id
print(chr(233))
print(chr(0xe9))
print(chr(0x1fc6))