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

print("---------------------------------------------------------------------")
'''
외부 데이터 교환 시, 문자열을 바이트로 인코딩/ 바이트를 문자열로 디코딩 의 과정이 필요하다.
UTF-8은 파이썬, 리눅스, HTML의 표준 텍스트 인코3딩이다.
유니코드 한 문자당 1~4바이트를 사용한다.
- 1바이트 : 아스키 코드
- 2바이트 : 키릴 문자를 제외한 대부분 파생된 라틴어
- 3바이트 : 기본 다국어 평면의 나머지
- 4바이트 : 아시아 언어 및 기호를 포함한 나머지
'''

snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8')
#ascii : 7비트 아스키 코드, latin-1 : ISO 8859-1로도 알려짐, cp-1252 윈도우 인코딩 형식
#UTF-8은 가변 길이 인코딩
print(len(ds))
print(ds)

#아스키로 인코딩 시, 아스키 코드가 아닌 문자를 해결하기 위해 두번째 인수 추가
print(snowman.encode('ascii','ignore'))
print(snowman.encode('ascii','replace'))
print(snowman.encode('ascii','backslashreplace'))
print(snowman.encode('ascii','xmlcharrefreplace'))
print("---------------------------------------------------------------------")

'''<디코딩>
 외부 소스에서 텍스트를 얻을 때마다 그것은 바이트 문자열로 인코딩되어 있다.
 실제로 어떤 인코딩이 사용되었는지 아는 것이 까다롭다'''

place = 'caf\u00e9'
print(place)
print(type(place))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
#디코딩
place2 = place_bytes.decode('utf-8')
print(place2)
#place2 = place_bytes.decode('ascii')
# 오류 발생 : 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
place4 = place_bytes.decode('latin-1')
print(place4)
place5 = place_bytes.decode('windows-1252')
print(place5)
print("---------------------------------------------------------------------")

'''HTML 엔티티: python 3.4에서 HTML 문자 엔티티를 사용하는 방법 추가'''
import html
print(html.unescape("&egrave;"))
#숫자로 된 엔티티 10진수나 16진수에도 적용
print(html.unescape("&#233;"))
print(html.unescape("&#xe9;"))

from html.entities import html5
print(html5["egrave"])
print(html5["egrave;"])

char = '\u00e9'
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])

place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value) #인코딩된 아스키 문자의 바이트 타입 반환
print(byte_value.decode()) #HTML 호환 문자열로 변환