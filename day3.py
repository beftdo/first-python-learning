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