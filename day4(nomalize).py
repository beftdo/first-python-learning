'''정규화
일부 유니코드 문자는 둘 이상의 유니코드 인코딩으로 표현된다. 모양은 같지만 
내부 시퀀스가 다르기 때문에 다르다.'''

eacute1 = 'é' #UTF-8
eacute2 = '\u00e9' # 유니코드 코드 포인트
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}'
eacute4 = chr(233) #10진수 바이트 값
eacute5 = chr(0xe9) #16진수 바이트 값
print(eacute1, eacute2, eacute3, eacute4, eacute5)
print(eacute1 == eacute2 == eacute3 == eacute4 == eacute5)

import unicodedata
print(unicodedata.name(eacute1))
print(ord(eacute1))
print(0xe9)

eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"
print(eacute_combined1, eacute_combined2, eacute_combined3)
print(eacute_combined1 == eacute_combined2 == eacute_combined3)

print(eacute1 == eacute_combined1)

#첫번째 유니코드와 두번째 유니코드는 똑같이 생겼지만 다름, 두번째 인수는 e와 엑센트를 합쳐서 만든
#유니코드 텍스트 문자이기 때문에.

import unicodedata
eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)
#NFC = Normal Form, Composed 구성된 일반 형식
print(len(eacute_combined1)) # 정규화 전
print(len(eacute_normalized)) # 정규화 후
print(eacute_normalized == eacute1)
print(unicodedata.name(eacute_normalized))